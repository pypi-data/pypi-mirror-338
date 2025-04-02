"""
This module uses Lark to parse a CSG file, then simplifies
the CSG tree to generate GLTS Nodes that match the
hierarchy of the CSG model.

OpenSCAD Text objects may be used to label nodes to give
them meaning: this should pull through to e.g. Blender.

Most of the processing is done only on the top level items
in the tree - usually the transformations that assemble
the individual parts. Everything under a `color` should
be only minimally processed: this is why I've split the
logic into the `Transformer` (which runs bottom-up over
the whole tree) and the function `csg_tree_to_nodes` which
recurses top-down over the tree, but terminates at `color`
commands. The latter can have much more complicated processing
as it runs over far fewer nodes.
"""
# This can be removed when py3.9 is end of life
from __future__ import annotations

from importlib.resources import files
from dataclasses import dataclass, field

import logging
from typing import Any
import json
from lark import Lark, Transformer, Tree, v_args
from lark.tree import Meta
import numpy as np

from scad2gltf.types import FlatNode, IndexedNode, MeshFromCSG, MeshFromSTL

logger = logging.getLogger(__name__)
logger.setLevel("DEBUG")

grammar_file = files("scad2gltf") / "csg_grammar.lark"

csg_parser = Lark(
    grammar_file.read_text(),
    parser = "lalr",
    propagate_positions = True,
)

@dataclass
class CSGObject:
    """
    A dataclass to represent the data of CSG call (licluding all child calls)
    """
    name: str
    args: list
    kwargs: dict[str, Any]
    children: list # this can change to list[Self] once py3.10 is end of life
    metadata: Meta
    label: str | None = None


def process_arguments(arguments: Tree):
    """Split argument tokens into positional and keyword"""
    args = []
    kwargs = {}
    for arg in arguments.children:
        if arg is None:
            continue  # Not sure why this is needed
        k, v = arg
        if k:
            kwargs[k] = v
        else:
            args.append(v)
    return args, kwargs


class CSGUndefined:
    """
    Represents `undef` in a CSG file.
    """

class CSGTransformer(Transformer):
    """
    A lark.Transformer class for CSG files for transforming the
    tree parsed by lark.
    """
    @v_args(meta=True)
    def object(self, metadata, items):
        """
        Transform any "object" into a more useful structure.
        An object as defined in the lark file is anything of the form:
            call_name(arguments*){child_object();}
        or
            call_name(arguments*);
        A CSG file is made up of one top level object with other nesed objects
        """
        name, arguments = items[:2]
        args, kwargs = process_arguments(arguments)
        if len(items) == 3:  # if the object is followed by a block
            children = list(items[2])
        else:
            children = []
        # Groups with one child should be replaced with
        # the child (otherwise labels go wrong)
        if name in {"group", "union"} and len(children) == 1:
            return children[0]
        # If the first child is a label, extract it:
        label = None
        if len(children) > 1:
            if is_label(children[0]):
                label = read_label(children[0])
                del children[0]

        return CSGObject(
            name = name,
            args = args,
            kwargs = kwargs,
            children = children,
            metadata=metadata,
            label = label,
        )

    def argument(self, items):
        """
        Transform an argument to either be a tuple of wither
        (argument_name, value) or (None, value)
        """
        if len(items) == 1:
            return (None, items[0])
        if len(items) == 2:
            return tuple(items)
        raise ValueError(
            "Argument should be either a single item (a value) or two items "
            "(an argument name and a value)"
        )

    def ARGNAME(self, t): # pylint: disable=invalid-name
        """
        The argument name, transform to a string
        """
        return t.value

    def CNAME(self, t): # pylint: disable=invalid-name
        """
        The call name, transform to a string
        """
        return t.value

    def block(self, items):
        """Blocks are lists of objects, and
        happily items is always iterable,
        so we can use it directly"""
        return tuple(items)

    # Many of these are copied from the JSON example
    def string(self, s):
        """
        Unpack tuple and remove quotes from string
        """
        (s,) = s
        return s[1:-1]

    def number(self, n):
        """
        Unpack tuple containing number and convert to float
        """
        (n,) = n
        return float(n)

    list = list

    def true(self, _):
        """
        Simply replace with true in the code python True
        """
        return True

    def false(self, _):
        """
        Simply replace with false in the code python False
        """
        return False

    def undef(self, _):
        """
        Simply replace with `undef` in the code with a CSGUndefined object
        """
        return CSGUndefined()

def is_label(first_child):
    """
    Return true if this is a gltf label
    """
    if first_child.name == "text":
        text = first_child.kwargs["text"]
        if 'gltf-group-info-version' in text:
            return True
    return False

def read_label(first_child):
    """
    Read the gltf label
    """
    text = first_child.kwargs["text"]
    # Have to convert from single to double quotes as openscad
    # has a bug that doesn't allow esaped strings to CSG
    label_data = json.loads(text.replace("'", '"'))
    if label_data['gltf-group-info-version'] not in {1}:
        print("Warning: unrecognised gltf-group-info-version")
    return label_data['name']

@dataclass
class Node:
    """Represents a GLTF Node"""
    transform: np.ndarray
    label: str | None
    children: "list[Node | Mesh]"


@dataclass
class Mesh:
    """A CSG tree that should be rendered as a single mesh"""
    csgtree: CSGObject
    color: tuple[float, float, float, float]
    metadata: Meta
    label: str | None = None
    transform: np.ndarray = field(
        default_factory=(lambda: np.identity(4)),
    )



def csg_tree_to_nodes(obj: CSGObject):
    """Recursively convert the parsed CSG tree into nodes
    
    This is much heavier than the processing done by Lark,
    but will only run over the top of the tree, as it stops
    recursing when it hits the `color` statements.

    Each `multmatrix`, `group`, and `union` object will be
    converted to a `Node`.

    Nested `Node`s will be combined: for example a `group`
    that contains another `group` will become a single
    flat group with all of the children. Similarly, a `group`
    or `union` with only one child will be replaced by the 
    child. This is an attempt to create a meaningful
    hierarchy: the tree in most CSG files is much deeper
    than it needs to be, as OpenSCAD adds a lot of `group`
    objects.

    `multmatrix` nodes will also be combined: the matrices
    are multiplied together in this case, which preserves
    the transformation. This means that any number of
    `translate`, `rotate`, `scale`, etc. modules will
    be combined into a single transforming `Node`, which
    makes a nicer hierarchy in e.g. Blender.
    """
    if obj.name not in ["multmatrix", "group", "union"]:
        if obj.name == "color":
            color = tuple(obj.args[0])
        else:
            print("WARNING: meshes should start with `color`")
            color = (0.5, 0.5, 0.5, 1.0)
        return Mesh(
            obj,
            color=color,
            metadata=obj.metadata,
        )
    # Flatten nested group/union objects to minimise the
    # number of GLTS nodes generated
    children = []
    for c in obj.children:
        if c.name in {"group", "union"} and not c.label:
            for cc in c.children:
                children.append(csg_tree_to_nodes(cc))
        else:
            children.append(csg_tree_to_nodes(c))

    # Each node needs a matrix transform - this is the identity
    # except for multmatrix.
    transform = np.identity(4)
    if obj.name == "multmatrix":
        transform = np.array(obj.args[0])
        assert transform.shape == (4, 4)

    # combine nodes if there's only one child
    # NB this works if the child is a node or a mesh
    if len(children) == 1:
        child = children[0]
        if obj.label is None or child.label is None:
            child.transform = np.dot(transform, child.transform)
            child.label = obj.label or child.label
            return child

    return Node(
        transform = transform,
        label = obj.label,
        children = children,
    )


def flatten_tree(node: Node) -> list[IndexedNode | Mesh]:
    """Convert a tree structure into a flat list of
    IndexedNode objects

    In the flattened list Node objects are replaced
    by IndexedNode object, these objects reference
    their Children by index. This is a better match
    to the GLTF Node schema.

    Mesh objects are left unchanged - `extract_meshes`
    can be run on the flattened tree to convert these
    to MeshFromSTL
    
    Deduplication is not performed
    """
    flattened: list[IndexedNode | Mesh] = []
    flatten_node(node, flattened)
    return flattened


def flatten_node(
        node: Node,
        flattened: list[IndexedNode | Mesh],
    ) -> int:
    """Inner recursive fucntion that flattens a tree

    This function follows the tree starting from the
    given node, and recursively adds it and all its
    children to the provided list `flattened`. The
    return value is the index of the node in the list,
    currently always zero and thus not useful.

    This returns the index of the node in the flattened list.
    use `flatten_tree` to get the list.
    """
    index = len(flattened)
    indexed_node = IndexedNode(
        matrix = node.transform,
        name = node.label,
        children = [],
    )
    flattened.append(indexed_node)
    child_indices = []
    for c in node.children:
        if isinstance(c, Node):
            # We recurse through nodes, and refer to
            # children by their index in `flattened`
            child_indices.append(flatten_node(c, flattened))
        else:
            child_indices.append(len(flattened))
            flattened.append(c)
    # Now we can fill in the child indices. This object
    # will be mutated in the list too, no need to reassign.
    indexed_node.children = child_indices
    return index


class NotAnImport(Exception):
    """Raised when the CSG tree is not an import"""


def mesh_from_import(mesh: Mesh) -> MeshFromSTL:
    """Use imported STL meshes directly
    
    If the supplied CSG tree generates its geometry only
    through an `import` statement, we don't need to render
    it, and can instead just use the STL. This is not only
    faster, it gets around some tricky path/portability
    issues with the CSG.
    
    If the supplied CSG tree is not an import, we raise
    a NotAnImport exception.
    """
    obj = mesh.csgtree
    transform = mesh.transform
    while True:
        if len(obj.children) > 1:
            raise NotAnImport()

        if obj.name in {"color", "group", "union"}:
            # These don't modify the mesh and may be
            # ignored, assuming there's one child.
            pass
        elif obj.name == "multmatrix":
            # Matrix transforms should be combined
            # and then we move to the child as above
            obj_tr = np.array(obj.args[0])
            transform = np.dot(transform, obj_tr)
        elif obj.name == "import":
            break
        else:
            raise NotAnImport()
        # If we get here, we want to work with the
        # single child of our node - if it's not there,
        # raise an error.
        if len(obj.children) != 1:
            raise NotAnImport()
        obj = obj.children[0]
    # obj should now be an import
    assert obj.name == "import"
    # Assume scale and origin are default
    assert obj.kwargs["scale"] == 1.0
    assert all(c == 0 for c in obj.kwargs["origin"])
    rel_fname = obj.kwargs["file"]
    # filenames are relative to the original SCAD file
    # so this may need rewritten
    print(f"Extracting {rel_fname} directly")
    return MeshFromSTL(
        fname=rel_fname,
        color=mesh.color,
        matrix=transform,
        name=rel_fname,
    )


def extract_meshes(
    nodes: list[IndexedNode | Mesh],
    csg_fname: str,
    scad_fname: str,
) -> list[FlatNode]:
    """
    For a given flattended list of Nodes replaces any Meshes with a mesh
    either with a MeshFromSTL object telling later processing to load the mesh
    directly from an STL file, or a MeshFromCSG object telling later processing
    to generate the STL file from CSG code via OpenSCAD.
    """
    with open(csg_fname, "r", encoding="utf-8") as f:
        csg_source = f.read()
    converted_nodes: list[FlatNode] = []
    for i, node in enumerate(nodes):
        if isinstance(node, IndexedNode):
            converted_nodes.append(node)
            continue
        try:
            # if the mesh is being imported from an STL,
            # use it directly and skip openscad.
            # this adds a MeshFromSTL
            converted_nodes.append(
                mesh_from_import(node)
            )
            continue
        except NotAnImport:
            pass
        mesh_fname = scad_fname + f".mesh_{i}.csg"
        print(f"Extracting {mesh_fname}")
        with open(mesh_fname, "w", encoding="utf-8") as f:
            f.write(
                csg_source[
                    node.metadata.start_pos:node.metadata.end_pos
                ]
            )
        assert isinstance(node.transform, np.ndarray), f"{mesh_fname} has bad transform"
        converted_nodes.append(
            MeshFromCSG(
                fname=mesh_fname,
                color=node.color,
                name=f"mesh_{i}",
                matrix=node.transform,
            )
        )
    assert len(converted_nodes) == len(nodes)
    return converted_nodes


def split_csg_file(
        filename: str,
        scad_fname: str,
    ) -> list[FlatNode]:
    """Load a CSG file, parse it, and split it into Nodes and Meshes
    
    This creates new csg files named `{scad_fname}.mesh_{i}.csg`
    """
    with open(filename, "r", encoding="utf-8") as f:
        csg_source = f.read()
    print(f"Parsing {filename}")
    node_tree = parse_csg_source(csg_source)
    nodes = flatten_tree(node_tree)
    return extract_meshes(
        nodes,
        csg_fname=filename,
        scad_fname=scad_fname,
    )

def parse_csg_source(csg_source):
    """
    Parse the csg source and return the node tree
    """
    tree = csg_parser.parse(csg_source)
    transformed = CSGTransformer().transform(tree)
    root = transformed.children[0]
    return csg_tree_to_nodes(root)


def print_csg_hierarchy(obj, prefix=""):
    """
    Recursive function to print the csg hierarchy
    """
    if isinstance(obj, Node):
        print(f"{prefix}{obj.label}")
        for c in obj.children:
            print_csg_hierarchy(c, prefix=prefix + "  ")

def prettyprint_nodes(node_list, index=0, prefix=""):
    """
    Recursive function to print nodes
    """
    obj = node_list[index]
    if isinstance(obj, (MeshFromCSG, MeshFromSTL)):
        print(f"{prefix}MESH: [name: {obj.name}, color: {obj.color}]")
    else:
        print(f"{prefix}Node -- {obj.name}")
        for child_index in obj.children:
            prettyprint_nodes(node_list, index=child_index, prefix=prefix + "  ")
