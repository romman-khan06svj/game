"""Main game engine class"""

import pygame
import sys
from typing import Dict, List
from dataclasses import dataclass
import yaml


@dataclass
class GameConfig:
    """Game configuration"""
    title: str
    width: int
    height: int
    fps: int
    fullscreen: bool = False


class GameEngine:
    """Main game engine"""

    def __init__(self, config_path: str = "config/settings.yaml"):
        """Initialize game engine
        
        Args:
            config_path: Path to configuration file
        """
        self.config = self._load_config(config_path)
        self.running = False
        self.paused = False
        
        # Initialize pygame
        pygame.init()
        self.display = self._init_display()
        self.clock = pygame.time.Clock()
        self.fps = self.config['game']['fps']
        
        # Game state
        self.world = None
        self.player = None
        self.camera = None
        self.ui = None
        
    @staticmethod
    def _load_config(config_path: str) -> Dict:
        """Load configuration from YAML file
        
        Args:
            config_path: Path to config file
            
        Returns:
            Configuration dictionary
        """
        try:
            with open(config_path, 'r') as f:
                return yaml.safe_load(f)
        except FileNotFoundError:
            print(f"Config file not found: {config_path}")
            return {}
    
    def _init_display(self) -> pygame.Surface:
        """Initialize pygame display
        
        Returns:
            Display surface
        """
        window_config = self.config.get('window', {})
        width = window_config.get('width', 1920)
        height = window_config.get('height', 1080)
        title = self.config.get('game', {}).get('title', 'Open World Game')
        
        flags = pygame.RESIZABLE if window_config.get('resizable') else 0
        if window_config.get('fullscreen'):
            flags |= pygame.FULLSCREEN
        
        display = pygame.display.set_mode((width, height), flags)
        pygame.display.set_caption(title)
        return display
    
    def handle_events(self) -> bool:
        """Handle game events
        
        Returns:
            True if game should continue running
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
                elif event.key == pygame.K_p:
                    self.paused = not self.paused
        
        return True
    
    def update(self, delta_time: float) -> None:
        """Update game state
        
        Args:
            delta_time: Time since last frame in seconds
        """
        if self.paused:
            return
        
        # Update world
        if self.world:
            self.world.update(delta_time)
        
        # Update player
        if self.player:
            self.player.update(delta_time)
        
        # Update camera
        if self.camera:
            self.camera.update()
    
    def render(self) -> None:
        """Render game frame"""
        # Clear display
        self.display.fill((0, 0, 0))
        
        # Render world
        if self.world:
            self.world.render(self.display, self.camera)
        
        # Render player
        if self.player:
            self.player.render(self.display, self.camera)
        
        # Render UI
        if self.ui:
            self.ui.render(self.display)
        
        # Update display
        pygame.display.flip()
    
    def run(self) -> None:
        """Main game loop"""
        self.running = True
        
        while self.running:
            # Handle events
            self.running = self.handle_events()
            
            # Calculate delta time
            delta_time = self.clock.tick(self.fps) / 1000.0
            
            # Update and render
            self.update(delta_time)
            self.render()
        
        self.quit()
    
    def quit(self) -> None:
        """Cleanup and quit"""
        pygame.quit()
        sys.exit()
