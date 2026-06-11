"""AI system"""

from typing import List
from ..entities import NPC


class AISystem:
    """Handles NPC AI and pathfinding"""
    
    def __init__(self):
        """Initialize AI system"""
        self.npcs: List[NPC] = []
    
    def add_npc(self, npc: NPC) -> None:
        """Add NPC to system
        
        Args:
            npc: NPC to add
        """
        self.npcs.append(npc)
    
    def remove_npc(self, npc: NPC) -> None:
        """Remove NPC from system
        
        Args:
            npc: NPC to remove
        """
        if npc in self.npcs:
            self.npcs.remove(npc)
    
    def update(self, delta_time: float) -> None:
        """Update all NPC AI
        
        Args:
            delta_time: Time since last frame
        """
        for npc in self.npcs:
            npc.update(delta_time)
