"""Collision system"""

from typing import List
from ..entities import Entity


class CollisionSystem:
    """Collision detection and response"""
    
    def __init__(self):
        """Initialize collision system"""
        self.collisions = []
    
    def check_collisions(self, entities: List[Entity]) -> List[tuple]:
        """Check for collisions
        
        Args:
            entities: List of entities to check
            
        Returns:
            List of collision pairs
        """
        collisions = []
        
        for i, entity1 in enumerate(entities):
            for entity2 in entities[i+1:]:
                if self._is_colliding(entity1, entity2):
                    collisions.append((entity1, entity2))
        
        return collisions
    
    @staticmethod
    def _is_colliding(entity1: Entity, entity2: Entity) -> bool:
        """Check if two entities are colliding
        
        Args:
            entity1: First entity
            entity2: Second entity
            
        Returns:
            True if colliding
        """
        # Simple circle collision
        dx = entity1.transform.x - entity2.transform.x
        dy = entity1.transform.y - entity2.transform.y
        distance = (dx**2 + dy**2)**0.5
        return distance < 50  # Simple threshold
