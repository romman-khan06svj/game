"""Map class"""

from typing import List


class Map:
    """Game map"""
    
    def __init__(self, width: int, height: int, tile_size: int = 32):
        """Initialize map
        
        Args:
            width: Map width in tiles
            height: Map height in tiles
            tile_size: Size of each tile
        """
        self.width = width
        self.height = height
        self.tile_size = tile_size
        self.tiles: List[List] = [[0 for _ in range(width)] for _ in range(height)]
    
    def get_tile(self, x: int, y: int):
        """Get tile at position
        
        Args:
            x: X coordinate
            y: Y coordinate
            
        Returns:
            Tile value
        """
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.tiles[y][x]
        return None
    
    def set_tile(self, x: int, y: int, value):
        """Set tile at position
        
        Args:
            x: X coordinate
            y: Y coordinate
            value: Tile value
        """
        if 0 <= x < self.width and 0 <= y < self.height:
            self.tiles[y][x] = value
