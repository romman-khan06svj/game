"""Base entity class"""

import pygame
from dataclasses import dataclass
from typing import Tuple


@dataclass
class Transform:
    """Entity transform (position, rotation, scale)"""
    x: float = 0.0
    y: float = 0.0
    z: float = 0.0
    rotation: float = 0.0
    scale_x: float = 1.0
    scale_y: float = 1.0


class Entity:
    """Base class for all game entities"""
    
    def __init__(self, entity_id: str, x: float, y: float):
        """Initialize entity
        
        Args:
            entity_id: Unique entity identifier
            x: X position
            y: Y position
        """
        self.id = entity_id
        self.transform = Transform(x=x, y=y)
        self.velocity_x = 0.0
        self.velocity_y = 0.0
        self.active = True
        self.collider = None
    
    def update(self, delta_time: float) -> None:
        """Update entity
        
        Args:
            delta_time: Time since last frame
        """
        if not self.active:
            return
        
        # Apply velocity
        self.transform.x += self.velocity_x * delta_time
        self.transform.y += self.velocity_y * delta_time
    
    def render(self, surface: pygame.Surface, camera) -> None:
        """Render entity
        
        Args:
            surface: Display surface
            camera: Camera object
        """
        pass
    
    def set_position(self, x: float, y: float) -> None:
        """Set entity position
        
        Args:
            x: X position
            y: Y position
        """
        self.transform.x = x
        self.transform.y = y
    
    def get_position(self) -> Tuple[float, float]:
        """Get entity position
        
        Returns:
            Tuple of (x, y)
        """
        return (self.transform.x, self.transform.y)
    
    def set_velocity(self, vx: float, vy: float) -> None:
        """Set entity velocity
        
        Args:
            vx: X velocity
            vy: Y velocity
        """
        self.velocity_x = vx
        self.velocity_y = vy
    
    def get_velocity(self) -> Tuple[float, float]:
        """Get entity velocity
        
        Returns:
            Tuple of (vx, vy)
        """
        return (self.velocity_x, self.velocity_y)
