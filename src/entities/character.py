"""Character entity class"""

import pygame
from .entity import Entity
from dataclasses import dataclass


@dataclass
class CharacterStats:
    """Character statistics"""
    health: int = 100
    max_health: int = 100
    armor: int = 0
    stamina: float = 100.0
    max_stamina: float = 100.0
    strength: int = 5
    speed: int = 5
    accuracy: int = 5


class Character(Entity):
    """Base character class"""
    
    def __init__(self, character_id: str, x: float, y: float, name: str):
        """Initialize character
        
        Args:
            character_id: Unique character identifier
            x: X position
            y: Y position
            name: Character name
        """
        super().__init__(character_id, x, y)
        self.name = name
        self.stats = CharacterStats()
        self.inventory = []
        self.equipped_weapon = None
        self.in_combat = False
        self.animation_state = "idle"
        self.animation_time = 0.0
    
    def take_damage(self, damage: int) -> None:
        """Take damage
        
        Args:
            damage: Damage amount
        """
        actual_damage = max(0, damage - self.stats.armor // 2)
        self.stats.health = max(0, self.stats.health - actual_damage)
        
        if self.stats.health <= 0:
            self.die()
    
    def die(self) -> None:
        """Character dies"""
        self.active = False
        self.animation_state = "dead"
    
    def heal(self, amount: int) -> None:
        """Heal character
        
        Args:
            amount: Healing amount
        """
        self.stats.health = min(self.stats.max_health, self.stats.health + amount)
    
    def add_to_inventory(self, item) -> None:
        """Add item to inventory
        
        Args:
            item: Item to add
        """
        self.inventory.append(item)
    
    def remove_from_inventory(self, item) -> None:
        """Remove item from inventory
        
        Args:
            item: Item to remove
        """
        if item in self.inventory:
            self.inventory.remove(item)
    
    def update(self, delta_time: float) -> None:
        """Update character
        
        Args:
            delta_time: Time since last frame
        """
        super().update(delta_time)
        
        # Update animation
        self.animation_time += delta_time
        
        # Regenerate stamina
        if self.stats.stamina < self.stats.max_stamina:
            self.stats.stamina = min(
                self.stats.max_stamina,
                self.stats.stamina + 10 * delta_time
            )
