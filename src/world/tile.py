"""Tile class"""

from enum import Enum
from dataclasses import dataclass


class TileType(Enum):
    """Tile types"""
    GRASS = 0
    ROAD = 1
    WATER = 2
    FOREST = 3
    BUILDING = 4
    MOUNTAIN = 5


@dataclass
class Tile:
    """Game tile"""
    tile_type: TileType
    walkable: bool = True
    drivable: bool = False
    height: float = 0.0
