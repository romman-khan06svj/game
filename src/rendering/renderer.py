"""Game renderer for visual output"""

import pygame
from typing import Optional


class Renderer:
    """Handles all game rendering"""
    
    def __init__(self, screen: pygame.Surface):
        """Initialize renderer
        
        Args:
            screen: Pygame display surface
        """
        self.screen = screen
        self.font_small = pygame.font.Font(None, 24)
        self.font_large = pygame.font.Font(None, 36)
    
    def draw_entity(self, entity, camera) -> None:
        """Draw an entity on screen
        
        Args:
            entity: Entity to draw
            camera: Camera object
        """
        # Calculate screen position
        screen_x = entity.transform.x - camera.x
        screen_y = entity.transform.y - camera.y
        
        # Only draw if on screen
        if -50 < screen_x < self.screen.get_width() + 50 and \
           -50 < screen_y < self.screen.get_height() + 50:
            
            # Draw circle for entity
            color = (0, 255, 0)  # Green for player
            if entity.id.startswith('npc'):
                color = (255, 0, 0)  # Red for NPCs
            elif hasattr(entity, 'vehicle_type'):
                color = (0, 0, 255)  # Blue for vehicles
            
            pygame.draw.circle(self.screen, color, (int(screen_x), int(screen_y)), 10)
            
            # Draw health bar if damaged
            if hasattr(entity, 'stats') and entity.stats.health < entity.stats.max_health:
                self._draw_health_bar(screen_x, screen_y, entity)
    
    def _draw_health_bar(self, x: float, y: float, entity) -> None:
        """Draw health bar above entity
        
        Args:
            x: Screen X position
            y: Screen Y position
            entity: Entity with health
        """
        bar_width = 20
        bar_height = 4
        health_ratio = entity.stats.health / entity.stats.max_health
        
        # Background (red)
        pygame.draw.rect(self.screen, (255, 0, 0), 
                        (x - bar_width/2, y - 20, bar_width, bar_height))
        # Health (green)
        pygame.draw.rect(self.screen, (0, 255, 0), 
                        (x - bar_width/2, y - 20, bar_width * health_ratio, bar_height))
    
    def draw_text(self, text: str, x: int, y: int, color=(255, 255, 255), 
                  large: bool = False) -> None:
        """Draw text on screen
        
        Args:
            text: Text to draw
            x: X position
            y: Y position
            color: Text color (RGB)
            large: Use large font
        """
        font = self.font_large if large else self.font_small
        surface = font.render(text, True, color)
        self.screen.blit(surface, (x, y))
    
    def draw_grid(self, camera, grid_size: int = 50) -> None:
        """Draw debug grid
        
        Args:
            camera: Camera object
            grid_size: Grid cell size
        """
        start_x = int(camera.x // grid_size) * grid_size
        start_y = int(camera.y // grid_size) * grid_size
        
        width = self.screen.get_width()
        height = self.screen.get_height()
        
        # Draw vertical lines
        x = start_x
        while x - camera.x < width:
            pygame.draw.line(self.screen, (50, 50, 50), 
                            (int(x - camera.x), 0), 
                            (int(x - camera.x), height))
            x += grid_size
        
        # Draw horizontal lines
        y = start_y
        while y - camera.y < height:
            pygame.draw.line(self.screen, (50, 50, 50), 
                            (0, int(y - camera.y)), 
                            (width, int(y - camera.y)))
            y += grid_size
    
    def clear(self, color=(34, 139, 34)) -> None:
        """Clear screen
        
        Args:
            color: Background color (RGB)
        """
        self.screen.fill(color)
