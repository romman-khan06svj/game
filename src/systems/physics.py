"""Physics system"""

from typing import List
from ..entities import Entity


class PhysicsSystem:
    """Physics simulation"""
    
    def __init__(self, gravity: float = 9.81, friction: float = 0.95):
        """Initialize physics system
        
        Args:
            gravity: Gravity acceleration
            friction: Friction coefficient
        """
        self.gravity = gravity
        self.friction = friction
    
    def update(self, entities: List[Entity], delta_time: float) -> None:
        """Update physics
        
        Args:
            entities: List of entities to update
            delta_time: Time since last frame
        """
        for entity in entities:
            # Apply friction
            entity.velocity_x *= self.friction
            entity.velocity_y *= self.friction
