"""Collision helper functions"""

from typing import Tuple


def distance(p1: Tuple[float, float], p2: Tuple[float, float]) -> float:
    """Calculate distance between two points
    
    Args:
        p1: First point (x, y)
        p2: Second point (x, y)
        
    Returns:
        Distance
    """
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    return (dx**2 + dy**2)**0.5


def normalize(vector: Tuple[float, float]) -> Tuple[float, float]:
    """Normalize a vector
    
    Args:
        vector: Vector (x, y)
        
    Returns:
        Normalized vector
    """
    mag = (vector[0]**2 + vector[1]**2)**0.5
    if mag == 0:
        return (0, 0)
    return (vector[0] / mag, vector[1] / mag)
