"""Player entity class"""

import pygame
from .character import Character


class Player(Character):
    """Player character"""
    
    def __init__(self, x: float, y: float, name: str = "Player"):
        """Initialize player
        
        Args:
            x: X position
            y: Y position
            name: Player name
        """
        super().__init__("player", x, y, name)
        self.in_vehicle = False
        self.current_vehicle = None
        self.is_sprinting = False
        self.base_speed = 150
        self.sprint_speed = 300
    
    def handle_input(self) -> None:
        """Handle player input"""
        keys = pygame.key.get_pressed()
        
        # Movement
        vx = 0
        vy = 0
        
        if keys[pygame.K_w]:
            vy -= self.base_speed
        if keys[pygame.K_s]:
            vy += self.base_speed
        if keys[pygame.K_a]:
            vx -= self.base_speed
        if keys[pygame.K_d]:
            vx += self.base_speed
        
        # Sprint
        if keys[pygame.K_LSHIFT]:
            self.is_sprinting = True
            multiplier = self.sprint_speed / self.base_speed
            vx *= multiplier
            vy *= multiplier
        else:
            self.is_sprinting = False
        
        self.set_velocity(vx, vy)
        
        # Update animation state
        if vx != 0 or vy != 0:
            self.animation_state = "run" if self.is_sprinting else "walk"
        else:
            self.animation_state = "idle"
    
    def enter_vehicle(self, vehicle) -> None:
        """Enter a vehicle
        
        Args:
            vehicle: Vehicle to enter
        """
        self.in_vehicle = True
        self.current_vehicle = vehicle
        self.active = False
    
    def exit_vehicle(self) -> None:
        """Exit current vehicle"""
        if self.current_vehicle:
            exit_pos = self.current_vehicle.get_exit_position()
            self.set_position(*exit_pos)
            self.current_vehicle = None
            self.in_vehicle = False
            self.active = True
    
    def update(self, delta_time: float) -> None:
        """Update player
        
        Args:
            delta_time: Time since last frame
        """
        if self.in_vehicle:
            return
        
        self.handle_input()
        super().update(delta_time)
