"""
This is the main file that runs if you run scad2gltf from terminal
"""

import os
import argparse
from tqdm.auto import tqdm
from scad2gltf.gltf import Gltf
from scad2gltf.openscad import scad2csg, csg2stl
from scad2gltf.parse_csg import split_csg_file
from scad2gltf.types import MeshFromCSG, MeshFromSTL

def main() -> None:
    """This is what runs if you run `scad2gltf` from the terminal
    """

    parser = argparse.ArgumentParser(description='Convert .scad file into .gltf')
    parser.add_argument('scadfile',
                        help='Path of the .scad file')
    parser.add_argument('-o', help='Specify output path (optional)')
    parser.add_argument(
        '--markers',
        action='store_true',
        help='Set SHOW_GLTF_MARKERS=true when running OpenSCAD'
    )

    [args, scad_args] = parser.parse_known_args()
    if args.markers:
        scad_args.append('-D')
        scad_args.append('SHOW_GLTF_MARKERS=true')

    csgfile = scad2csg(args.scadfile, scad_args)
    nodes = split_csg_file(csgfile, scad_fname=args.scadfile)
    # Adjust STL paths so they are absolute
    for node in nodes:
        if isinstance(node, MeshFromSTL):
            # The path is relative to the OpenSCAD file
            node.fname = os.path.normpath(
                os.path.join(
                    os.path.dirname(args.scadfile),
                    node.fname,
                )
            )
    # Find each MeshFromCSG node in the list of nodes. These are the STLs that
    # need to be generated
    csg_indices = [i for i, n in enumerate(nodes) if isinstance(n, MeshFromCSG)]
    for i in tqdm(csg_indices, desc="Rendering CSG to STL"):
        node = nodes[i]
        assert isinstance(node, MeshFromCSG)
        tqdm.write(f"Processing {node.fname}")
        nodes[i] = MeshFromSTL(
            fname=csg2stl(node.fname),
            color=node.color,
            name=node.name,
            matrix=node.matrix,
        )
    if args.o:
        gltffile = args.o
    else:
        gltffile = args.scadfile[:-4] + 'glb'
    gltf = Gltf(nodes)
    gltf.save(gltffile)
