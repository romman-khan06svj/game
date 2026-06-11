"""Non-Player Character entity class"""

import pygame
from .character import Character
import random


class NPCBehavior:
    """NPC behavior state"""
    IDLE = "idle"
    PATROL = "patrol"
    FOLLOW = "follow"
    COMBAT = "combat"
    FLEE = "flee"


class NPC(Character):
    """Non-player character"""
    
    def __init__(self, npc_id: str, x: float, y: float, name: str):
        """Initialize NPC
        
        Args:
            npc_id: Unique NPC identifier
            x: X position
            y: Y position
            name: NPC name
        """
        super().__init__(npc_id, x, y, name)
        self.behavior = NPCBehavior.IDLE
        self.behavior_timer = 0.0
        self.patrol_points = []
        self.current_patrol_index = 0
        self.view_distance = 500
        self.speed = 100
    
    def set_patrol_route(self, points: list) -> None:
        """Set NPC patrol route
        
        Args:
            points: List of (x, y) positions to patrol
        """
        self.patrol_points = points
        self.current_patrol_index = 0
    
    def patrol(self, delta_time: float) -> None:
        """Execute patrol behavior
        
        Args:
            delta_time: Time since last frame
        """
        if not self.patrol_points:
            self.behavior = NPCBehavior.IDLE
            return
        
        target = self.patrol_points[self.current_patrol_index]
        
        # Move towards target
        dx = target[0] - self.transform.x
        dy = target[1] - self.transform.y
        distance = (dx**2 + dy**2)**0.5
        
        if distance < 10:
            # Reached target, move to next
            self.current_patrol_index = (self.current_patrol_index + 1) % len(self.patrol_points)
        else:
            # Move towards target
            norm = distance / (distance + 0.001)
            self.velocity_x = dx * norm * self.speed
            self.velocity_y = dy * norm * self.speed
            self.animation_state = "walk"
    
    def look_around(self) -> None:
        """Check for nearby entities"""
        # This would be called to look for player or other NPCs
        pass
    
    def update(self, delta_time: float) -> None:
        """Update NPC
        
        Args:
            delta_time: Time since last frame
        """
        super().update(delta_time)
        
        self.behavior_timer += delta_time
        
        # Execute behavior
        if self.behavior == NPCBehavior.IDLE:
            if self.behavior_timer > random.uniform(3, 8):
                if self.patrol_points:
                    self.behavior = NPCBehavior.PATROL
                self.behavior_timer = 0
        elif self.behavior == NPCBehavior.PATROL:
            self.patrol(delta_time)
