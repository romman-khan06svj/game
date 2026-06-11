"""World class"""

import pygame
from typing import List, Dict
from ..entities import Entity


class World:
    """Game world"""
    
    def __init__(self, width: int, height: int):
        """Initialize world
        
        Args:
            width: World width
            height: World height
        """
        self.width = width
        self.height = height
        self.entities: Dict[str, Entity] = {}
        self.background_color = (34, 139, 34)  # Forest green
    
    def add_entity(self, entity: Entity) -> None:
        """Add entity to world
        
        Args:
            entity: Entity to add
        """
        self.entities[entity.id] = entity
    
    def remove_entity(self, entity_id: str) -> None:
        """Remove entity from world
        
        Args:
            entity_id: ID of entity to remove
        """
        if entity_id in self.entities:
            del self.entities[entity_id]
    
    def get_entity(self, entity_id: str) -> Entity:
        """Get entity by ID
        
        Args:
            entity_id: Entity ID
            
        Returns:
            Entity or None
        """
        return self.entities.get(entity_id)
    
    def get_nearby_entities(self, x: float, y: float, radius: float) -> List[Entity]:
        """Get entities within radius
        
        Args:
            x: Center X position
            y: Center Y position
            radius: Search radius
            
        Returns:
            List of nearby entities
        """
        nearby = []
        for entity in self.entities.values():
            dx = entity.transform.x - x
            dy = entity.transform.y - y
            distance = (dx**2 + dy**2)**0.5
            if distance <= radius:
                nearby.append(entity)
        return nearby
    
    def update(self, delta_time: float) -> None:
        """Update world
        
        Args:
            delta_time: Time since last frame
        """
        for entity in list(self.entities.values()):
            if entity.active:
                entity.update(delta_time)
    
    def render(self, surface: pygame.Surface, camera) -> None:
        """Render world
        
        Args:
            surface: Display surface
            camera: Camera object
        """
        # Draw background
        surface.fill(self.background_color)
        
        # Draw grid for debugging
        self._draw_grid(surface, camera)
        
        # Draw entities
        for entity in self.entities.values():
            if entity.active:
                entity.render(surface, camera)
    
    @staticmethod
    def _draw_grid(surface: pygame.Surface, camera, grid_size: int = 50) -> None:
        """Draw debug grid
        
        Args:
            surface: Display surface
            camera: Camera object
            grid_size: Grid cell size
        """
        # Simple grid drawing
        pass
