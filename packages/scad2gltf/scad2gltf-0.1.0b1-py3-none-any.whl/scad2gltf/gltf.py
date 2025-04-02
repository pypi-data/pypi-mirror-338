'''
This module create the GLTF from nodes that are read from the CSG file. These nodes
contain references to STL files which are changed into GLTF meshes

This was originally adapted from:
https://stackoverflow.com/questions/66341118/how-do-i-import-an-stl-into-pygltflib
it has changed quite a bit since then
'''
from dataclasses import dataclass
import pygltflib
import numpy as np
import stl


from scad2gltf.types import IndexedNode, MeshFromSTL

def stl2mesh(stlfile):
    """
    Converts an stl file into a mesh for a glb.
    """
    stl_mesh = stl.mesh.Mesh.from_file(stlfile)

    stl_points = []
    for stl_mesh.point in stl_mesh.points: # Convert points into correct numpy array
        stl_points.append([stl_mesh.point[0],stl_mesh.point[1],stl_mesh.point[2]])
        stl_points.append([stl_mesh.point[3],stl_mesh.point[4],stl_mesh.point[5]])
        stl_points.append([stl_mesh.point[6],stl_mesh.point[7],stl_mesh.point[8]])

    points = np.array(
        stl_points,
        dtype="float32",
    )

    stl_normals = []
    for normal in stl_mesh.normals:
        magnitude = np.sqrt(np.sum(normal**2))
        if magnitude<1e-10:
            #Give zero magnitude elements and aribary unit vector to keep GLTF format happy
            normal_vector = np.asarray([1,0,0])
        else:
            normal_vector = normal/magnitude
        stl_normals.append(normal_vector)
        stl_normals.append(normal_vector)
        stl_normals.append(normal_vector)

    normals = np.array(
        stl_normals,
        dtype="float32"
    )
    return points, normals

def node_for_mesh(
        mesh: MeshFromSTL, mesh_i: int
    ) -> pygltflib.Node:
    """Create a GLTF node for a mesh."""
    return pygltflib.Node(
        mesh=mesh_i,
        name=mesh.name,
        matrix=list(mesh.matrix.T.flat),
    )

@dataclass
class Material:
    """
    A data class to store material properties before they are converted
    into GLTF materials. This allows deduplication
    """
    color: tuple[float, float, float, float]
    metallic_factor: float = .5
    roughness_factor: float = .5

    def __post_init__(self):
        assert len(self.color) == 4, "Colour should be 4 floats"
        self.color = tuple(self.color)

class Gltf:
    """
    A class for writng GLTFs from nodes
    """

    def  __init__(self, internal_nodes: list[IndexedNode, MeshFromSTL]):
        self.nodes = []
        self.meshes = []
        # mesh files is a dictionary with file names as keys
        self.mesh_files = {}
        self.bufferviews = []
        self.accessors = []
        self.materials = []
        self.running_buffer_len=0
        self.blob = None

        self._add_nodes(internal_nodes)


    def _add_nodes(self, internal_nodes: list[IndexedNode, MeshFromSTL]):
        """
        This takes a list of our internal way of stroing nodes and loads
        them into the correct format for saving as a GLTF with .save()
        """

        for internal_node in internal_nodes:
            if isinstance(internal_node, IndexedNode):
                # If an indexed node a convert our dataclass to pygltflib.Node
                self.nodes.append(
                    pygltflib.Node(
                        matrix=list(internal_node.matrix.T.flat),
                        children=internal_node.children,
                        name=internal_node.name,
                    )
                )
            else:
                # If not it is an STL node. Process this
                self._process_stl_node(internal_node)

    def _process_stl_node(self, stl_node: MeshFromSTL):
        assert isinstance(stl_node, MeshFromSTL)

        if stl_node.fname in self.mesh_files:
            #If stl is already used. Reload the position of the data in the buffer
            points_buf_no =  self.mesh_files[stl_node.fname]["points_buf_no"]
            normals_buf_no =  self.mesh_files[stl_node.fname]["normals_buf_no"]
        else:
            points_buf_no, normals_buf_no = self._add_stl_geometry(stl_node)

            self.mesh_files[stl_node.fname] = {"points_buf_no": points_buf_no,
                                               "normals_buf_no": normals_buf_no}

        material = Material(stl_node.color, metallic_factor=.5, roughness_factor=0.3)
        if material not in self.materials:
            material_index = len(self.materials)
            self.materials.append(material)
        else:
            material_index = self.materials.index(material)

        attribute = pygltflib.Attributes(POSITION=points_buf_no, NORMAL=normals_buf_no)
        primitive = pygltflib.Primitive(attributes=attribute,
                                        indices=None,
                                        material=material_index)
        self.meshes.append(pygltflib.Mesh(primitives=[primitive]))

        self.nodes.append(node_for_mesh(stl_node, len(self.meshes)-1))


    def _add_stl_geometry(self, stl_node):
        """
        Takeing in the STL node. Load in the geomtry and save it to the buffers
        return the buffer view number for the points buffer and the normals buffer
        as a tupple
        """
        points, normals = stl2mesh(stl_node.fname)

        points_buf_no = len(self.bufferviews)
        points_accessor = pygltflib.Accessor(bufferView=points_buf_no,
                                             componentType=pygltflib.FLOAT,
                                             count=len(points),
                                             type=pygltflib.VEC3,
                                             max=points.max(axis=0).tolist(),
                                             min=points.min(axis=0).tolist())
        self.accessors.append(points_accessor)
        self.add_to_buffer(points)

        normals_buf_no = len(self.bufferviews)
        normals_accessor = pygltflib.Accessor(bufferView=normals_buf_no,
                                              componentType=pygltflib.FLOAT,
                                              count=len(normals),
                                              type=pygltflib.VEC3,
                                              max=None,
                                              min=None)

        self.accessors.append(normals_accessor)
        self.add_to_buffer(normals)
        return points_buf_no, normals_buf_no

    def add_to_buffer(self, data):
        """
        Add numpy data to the bunarry buffer
        """
        binary_blob = data.tobytes()
        buffer = pygltflib.BufferView(buffer=0,
                                      byteOffset=self.running_buffer_len,
                                      byteLength=len(binary_blob),
                                      target=pygltflib.ARRAY_BUFFER)
        self.running_buffer_len += len(binary_blob)
        self.bufferviews.append(buffer)
        if self.blob is None:
            self.blob = binary_blob
        else:
            self.blob += binary_blob

    def gltf_materials(self):
        """
        return the list of gltf materials
        """

        def darken(col, factor=2):
            return (col[0]/factor, col[1]/factor, col[2]/factor, col[3])

        gltf_materials = []
        for i, material in enumerate(self.materials):
            pbr_metal = pygltflib.PbrMetallicRoughness(
                baseColorFactor = darken(material.color),
                metallicFactor=material.metallic_factor,
                roughnessFactor=material.roughness_factor)
            gltf_materials.append(
                pygltflib.Material(
                    pbrMetallicRoughness=pbr_metal,
                    name=f"color{i}",
                    emissiveFactor=[0, 0, 0],
                    alphaCutoff=None,
                    doubleSided=True
                )
            )
        return gltf_materials

    def save(self, gltffile):
        """
        Save as a GLTF file
        """
        gltf = pygltflib.GLTF2(
            scene=0,
            scenes=[pygltflib.Scene(nodes=[0])],
            nodes=self.nodes,
            meshes=self.meshes,
            materials=self.gltf_materials(),
            accessors=self.accessors,
            bufferViews=self.bufferviews,
            buffers=[pygltflib.Buffer(byteLength=self.running_buffer_len)],
        )
        gltf.set_binary_blob(self.blob)
        gltf.save(gltffile)
