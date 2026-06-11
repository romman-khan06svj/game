#!/usr/bin/env python3
"""Game entry point"""

import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

from src.core.game_engine import GameEngine
from src.world.world import World
from src.entities.player import Player
from src.entities.npc import NPC
from src.ui.hud import HUD


class Game:
    """Main game class"""
    
    def __init__(self):
        """Initialize game"""
        self.engine = GameEngine()
        self._init_game()
    
    def _init_game(self) -> None:
        """Initialize game world and entities"""
        # Create world
        self.engine.world = World(2000, 2000)
        
        # Create player
        self.engine.player = Player(100, 100, "Player")
        self.engine.world.add_entity(self.engine.player)
        
        # Create some NPCs
        for i in range(5):
            npc = NPC(f"npc_{i}", 200 + i * 100, 200, f"NPC_{i}")
            npc.set_patrol_route([
                (200 + i * 100, 200),
                (300 + i * 100, 200),
                (300 + i * 100, 300),
                (200 + i * 100, 300),
            ])
            self.engine.world.add_entity(npc)
        
        # Create UI
        self.engine.ui = HUD()
        
        # Create a simple camera (center on player)
        class SimpleCamera:
            def __init__(self, player):
                self.player = player
                self.x = 0
                self.y = 0
            
            def update(self):
                self.x = self.player.transform.x - 960
                self.y = self.player.transform.y - 540
        
        self.engine.camera = SimpleCamera(self.engine.player)
    
    def run(self) -> None:
        """Run the game"""
        print("Starting Open World Game...")
        print("Controls:")
        print("  WASD - Move")
        print("  Shift - Sprint")
        print("  ESC - Quit")
        print("  P - Pause")
        
        self.engine.run()


if __name__ == "__main__":
    game = Game()
    game.run()
