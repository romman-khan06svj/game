"""Event system for game communication"""

from typing import Callable, Dict, List, Any
from dataclasses import dataclass


@dataclass
class GameEvent:
    """Base game event"""
    event_type: str
    data: Dict[str, Any] = None


class EventManager:
    """Manages game events and subscriptions"""
    
    def __init__(self):
        """Initialize event manager"""
        self.subscribers: Dict[str, List[Callable]] = {}
    
    def subscribe(self, event_type: str, callback: Callable) -> None:
        """Subscribe to event
        
        Args:
            event_type: Type of event to subscribe to
            callback: Function to call when event fires
        """
        if event_type not in self.subscribers:
            self.subscribers[event_type] = []
        self.subscribers[event_type].append(callback)
    
    def unsubscribe(self, event_type: str, callback: Callable) -> None:
        """Unsubscribe from event
        
        Args:
            event_type: Type of event
            callback: Function to remove
        """
        if event_type in self.subscribers:
            self.subscribers[event_type].remove(callback)
    
    def emit(self, event: GameEvent) -> None:
        """Emit an event
        
        Args:
            event: Event to emit
        """
        if event.event_type in self.subscribers:
            for callback in self.subscribers[event.event_type]:
                callback(event)
