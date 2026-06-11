#!/usr/bin/env python3
"""Game entry point with all systems"""

import sys
import os
import pygame

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

from src.core.game_engine import GameEngine
from src.world.world import World
from src.entities.player import Player
from src.entities.npc import NPC
from src.entities.vehicle import Vehicle
from src.ui.hud import HUD
from src.systems.combat import CombatSystem
from src.systems.vehicle import VehicleSystem
from src.systems.missions import MissionManager


class Game:
    """Main game class with all systems"""
    
    def __init__(self):
        """Initialize game"""
        self.engine = GameEngine()
        
        # Initialize game systems
        self.combat_system = CombatSystem()
        self.vehicle_system = VehicleSystem()
        self.mission_manager = MissionManager()
        
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
        
        # Create vehicles
        vehicle1 = Vehicle("vehicle_1", 500, 500, "car")
        vehicle1.stats.speed = 500
        self.engine.world.add_entity(vehicle1)
        self.vehicle_system.add_vehicle(vehicle1)
        
        vehicle2 = Vehicle("vehicle_2", 800, 500, "bike")
        vehicle2.stats.speed = 450
        self.engine.world.add_entity(vehicle2)
        self.vehicle_system.add_vehicle(vehicle2)
        
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
        
        # Start first mission
        self.mission_manager.start_mission("mission_explore")
    
    def handle_player_input(self) -> None:
        """Handle player input for combat and vehicle"""
        keys = pygame.key.get_pressed()
        
        # Combat input
        if keys[pygame.K_f]:
            # Attack nearby NPCs
            nearby = self.engine.world.get_nearby_entities(
                self.engine.player.transform.x,
                self.engine.player.transform.y,
                100
            )
            
            for entity in nearby:
                if entity.id.startswith('npc'):
                    self.combat_system.player_attack(self.engine.player, entity)
        
        # Vehicle input
        if self.engine.player.in_vehicle and self.engine.player.current_vehicle:
            self.vehicle_system.handle_vehicle_input(
                self.engine.player.current_vehicle, 
                keys
            )
        
        # Vehicle interactions
        if keys[pygame.K_e]:
            nearby = self.engine.world.get_nearby_entities(
                self.engine.player.transform.x,
                self.engine.player.transform.y,
                50
            )
            
            for entity in nearby:
                if hasattr(entity, 'vehicle_type'):
                    if not self.engine.player.in_vehicle:
                        self.engine.player.enter_vehicle(entity)
                        entity.start_engine()
                        print(f"Entered {entity.vehicle_type}")
                    break
    
    def update(self, delta_time: float) -> None:
        """Update all game systems
        
        Args:
            delta_time: Time since last frame
        """
        # Handle player input for combat/vehicles
        self.handle_player_input()
        
        # Update engine (player movement, world entities)
        self.engine.update(delta_time)
        
        # Update vehicles
        if self.vehicle_system.vehicles:
            self.vehicle_system.update(
                self.vehicle_system.vehicles, 
                delta_time, 
                self.engine.world
            )
        
        # Update combat
        npcs = [e for e in self.engine.world.entities.values() if e.id.startswith('npc')]
        self.combat_system.update(self.engine.player, npcs, delta_time)
        
        # Update missions
        self.mission_manager.update(self.engine.player, self.engine.world, delta_time)
    
    def render(self) -> None:
        """Render game frame"""
        self.engine.render()
        
        # Render mission info
        active_missions = self.mission_manager.get_active_missions()
        if active_missions:
            mission = active_missions[0]
            mission_text = f"Mission: {mission.title} - {mission.get_progress():.0f}%"
            self.engine.renderer.draw_text(mission_text, 10, 100, (255, 255, 100))
        
        # Render vehicle info if in vehicle
        if self.engine.player.in_vehicle and self.engine.player.current_vehicle:
            vehicle = self.engine.player.current_vehicle
            fuel_text = f"Fuel: {vehicle.stats.fuel:.0f}/{vehicle.stats.max_fuel:.0f}"
            speed_text = f"Speed: {vehicle.current_speed:.0f}"
            self.engine.renderer.draw_text(fuel_text, 10, 130, (255, 100, 100))
            self.engine.renderer.draw_text(speed_text, 10, 160, (255, 100, 100))
        
        # Draw controls info
        self.engine.renderer.draw_text("F: Attack | E: Vehicle | P: Pause | ESC: Quit", 
                                       10, self.engine.display.get_height() - 30, 
                                       (200, 200, 200))
    
    def run(self) -> None:
        """Run the game"""
        print("=" * 60)
        print("🎮 OPEN WORLD GAME - GTA-LIKE 🎮")
        print("=" * 60)
        print("\n📖 CONTROLS:")
        print("  🎮 WASD - Move around the world")
        print("  🏃 Shift - Sprint (move faster)")
        print("  ⚔️  F - Attack nearby NPCs (hold key)")
        print("  🚗 E - Enter/Exit vehicles")
        print("  ⏸️  P - Pause the game")
        print("  ❌ ESC - Quit game")
        print("\n🎯 GAME SYSTEMS ACTIVE:")
        print("  ✅ Combat System - Fight NPCs!")
        print("     → Get close to NPC and press F")
        print("     → Each hit deals 15 damage")
        print("     → NPC fights back with 10 damage")
        print("  ✅ Vehicle System - Drive vehicles!")
        print("     → Find blue circles (cars/bikes)")
        print("     → Press E to enter")
        print("     → Use WASD to steer and drive")
        print("     → Watch fuel meter!")
        print("  ✅ Mission System - Complete objectives!")
        print("     → Mission 1: Explore (travel 500m + find 3 NPCs)")
        print("     → Mission 2: Survive (defeat 5 NPCs)")
        print("     → Rewards: Money + XP")
        print("\n📍 ENTITY LOCATIONS:")
        print("  🟢 Green Circle = You (Player)")
        print("  🔴 Red Circles = NPCs (patrol around)")
        print("  🔵 Blue Circles = Vehicles (car at 500,500 / bike at 800,500)")
        print("\n💡 GAMEPLAY TIPS:")
        print("  → Explore the map (2000x2000)")
        print("  → Find and attack NPCs")
        print("  → Drive vehicles to travel faster")
        print("  → Complete missions for rewards")
        print("  → Watch your health bar!")
        print("=" * 60)
        print()
        
        self.engine.running = True
        clock = pygame.time.Clock()
        fps_target = self.engine.fps
        
        while self.engine.running:
            # Handle events
            self.engine.running = self.engine.handle_events()
            
            # Calculate delta time
            delta_time = clock.tick(fps_target) / 1000.0
            self.engine.fps_display = clock.get_fps()
            
            # Update and render
            self.update(delta_time)
            self.render()
        
        self.engine.quit()


if __name__ == "__main__":
    game = Game()
    game.run()
