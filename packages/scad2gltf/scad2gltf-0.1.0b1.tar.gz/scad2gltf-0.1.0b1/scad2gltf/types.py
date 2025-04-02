"""
This module contains scad2gltf's dataclasses
"""
# This can be removed when py3.9 is end of life
from __future__ import annotations
# This can also be removed when py3.9 is end of life
# FlatNode can then use | rather than Union
from typing import Union

from dataclasses import dataclass, field
import numpy as np

@dataclass
class IndexedNode:
    """Represents a GLTS Node"""
    name: str | None
    children: list[int]
    matrix: np.ndarray = field(
        default_factory=lambda: np.identity(4),
    )


@dataclass
class MeshFromCSG:
    """A mesh node that will be populated from a CSG file"""
    fname: str
    color: tuple[float, float, float, float]
    name: str | None = None
    matrix: np.ndarray = field(
        default_factory=lambda: np.identity(4),
    )

@dataclass
class MeshFromSTL:
    """A mesh node that will be populated from a STL file"""
    fname: str
    color: tuple[float, float, float, float]
    name: str | None = None
    matrix: np.ndarray = field(
        default_factory=lambda: np.identity(4),
    )

FlatNode = Union[IndexedNode, MeshFromCSG, MeshFromSTL]
