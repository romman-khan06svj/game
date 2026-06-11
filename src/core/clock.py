"""Game clock and time management"""

from dataclasses import dataclass
from typing import Callable, List


@dataclass
class GameClock:
    """Manages game time and day/night cycle"""
    
    def __init__(self, day_length_seconds: float = 3600.0):
        """Initialize game clock
        
        Args:
            day_length_seconds: Length of one full day in seconds
        """
        self.elapsed_time = 0.0
        self.day_length = day_length_seconds
        self.hour = 6  # Start at 6 AM
        self.minute = 0
        self.listeners: List[Callable] = []
    
    def update(self, delta_time: float) -> None:
        """Update game time
        
        Args:
            delta_time: Time passed in seconds
        """
        self.elapsed_time += delta_time
        
        # Calculate hours and minutes
        total_minutes = (self.elapsed_time / self.day_length) * 24 * 60
        self.hour = int((6 + total_minutes // 60) % 24)
        self.minute = int(total_minutes % 60)
    
    def get_time_of_day(self) -> tuple:
        """Get current time
        
        Returns:
            Tuple of (hour, minute)
        """
        return (self.hour, self.minute)
    
    def get_day_progress(self) -> float:
        """Get progress through the day (0.0 to 1.0)
        
        Returns:
            Day progress ratio
        """
        return (self.elapsed_time % self.day_length) / self.day_length
    
    def is_night(self) -> bool:
        """Check if it's night time
        
        Returns:
            True if between 20:00 and 6:00
        """
        return self.hour >= 20 or self.hour < 6
    
    def add_listener(self, callback: Callable) -> None:
        """Add time change listener
        
        Args:
            callback: Function to call on time change
        """
        self.listeners.append(callback)
