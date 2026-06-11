"""Vector utilities"""

from dataclasses import dataclass
from typing import Tuple


@dataclass
class Vector2:
    """2D vector"""
    x: float = 0.0
    y: float = 0.0
    
    def __add__(self, other: 'Vector2') -> 'Vector2':
        """Vector addition"""
        return Vector2(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other: 'Vector2') -> 'Vector2':
        """Vector subtraction"""
        return Vector2(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar: float) -> 'Vector2':
        """Scalar multiplication"""
        return Vector2(self.x * scalar, self.y * scalar)
    
    def magnitude(self) -> float:
        """Get vector magnitude"""
        return (self.x**2 + self.y**2)**0.5
    
    def normalize(self) -> 'Vector2':
        """Normalize vector"""
        mag = self.magnitude()
        if mag == 0:
            return Vector2(0, 0)
        return Vector2(self.x / mag, self.y / mag)
    
    def to_tuple(self) -> Tuple[float, float]:
        """Convert to tuple"""
        return (self.x, self.y)
