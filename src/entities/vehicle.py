"""Vehicle entity class"""

import pygame
from .entity import Entity
from dataclasses import dataclass


@dataclass
class VehicleStats:
    """Vehicle statistics"""
    health: int = 100
    max_health: int = 100
    fuel: float = 100.0
    max_fuel: float = 100.0
    speed: float = 500.0
    acceleration: float = 200.0
    braking: float = 300.0


class Vehicle(Entity):
    """Vehicle entity"""
    
    def __init__(self, vehicle_id: str, x: float, y: float, vehicle_type: str):
        """Initialize vehicle
        
        Args:
            vehicle_id: Unique vehicle identifier
            x: X position
            y: Y position
            vehicle_type: Type of vehicle (car, bike, truck, etc.)
        """
        super().__init__(vehicle_id, x, y)
        self.vehicle_type = vehicle_type
        self.stats = VehicleStats()
        self.occupants = []
        self.is_running = False
        self.current_speed = 0.0
        self.acceleration = 0.0
    
    def start_engine(self) -> None:
        """Start vehicle engine"""
        if self.stats.fuel > 0:
            self.is_running = True
    
    def stop_engine(self) -> None:
        """Stop vehicle engine"""
        self.is_running = False
        self.current_speed = 0.0
    
    def accelerate(self, amount: float) -> None:
        """Accelerate vehicle
        
        Args:
            amount: Acceleration amount (-1.0 to 1.0)
        """
        if not self.is_running:
            return
        
        self.acceleration = amount * self.stats.acceleration
    
    def brake(self) -> None:
        """Apply brakes"""
        self.acceleration = -self.stats.braking
    
    def add_occupant(self, character) -> None:
        """Add character to vehicle
        
        Args:
            character: Character to add
        """
        self.occupants.append(character)
    
    def remove_occupant(self, character) -> None:
        """Remove character from vehicle
        
        Args:
            character: Character to remove
        """
        if character in self.occupants:
            self.occupants.remove(character)
    
    def get_exit_position(self):
        """Get exit position for occupants
        
        Returns:
            Tuple of (x, y)
        """
        return (self.transform.x + 50, self.transform.y)
    
    def update(self, delta_time: float) -> None:
        """Update vehicle
        
        Args:
            delta_time: Time since last frame
        """
        super().update(delta_time)
        
        if not self.is_running:
            return
        
        # Update speed
        self.current_speed += self.acceleration * delta_time
        self.current_speed = max(0, min(self.stats.speed, self.current_speed))
        
        # Consume fuel
        if self.current_speed > 0:
            fuel_consumption = (self.current_speed / self.stats.speed) * delta_time
            self.stats.fuel = max(0, self.stats.fuel - fuel_consumption)
            
            if self.stats.fuel <= 0:
                self.stop_engine()
