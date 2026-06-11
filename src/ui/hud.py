"""Heads-up display (HUD)"""

import pygame


class HUD:
    """Game HUD"""
    
    def __init__(self):
        """Initialize HUD"""
        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)
    
    def render(self, surface: pygame.Surface) -> None:
        """Render HUD
        
        Args:
            surface: Display surface
        """
        # Draw FPS counter
        fps_text = self.font.render("FPS: 60", True, (255, 255, 255))
        surface.blit(fps_text, (10, 10))
