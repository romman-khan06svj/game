# Open World Game (GTA-like)

A free-roaming, open-world game with multiple characters, dynamic gameplay, and interactive environments.

## Features

- **Free Roaming**: Explore a large open world without restrictions
- **Multiple Characters**: Play as different characters with unique abilities
- **Vehicle System**: Drive cars, bikes, and other vehicles
- **Mission System**: Complete various missions and side quests
- **Combat System**: Engage in combat with NPCs
- **Dynamic NPCs**: AI-controlled characters with routines and behaviors
- **Physics Engine**: Realistic movement and vehicle mechanics
- **Day/Night Cycle**: Dynamic lighting and time of day
- **Inventory System**: Collect items, weapons, and equipment

## Installation

```bash
pip install -r requirements.txt
```

## Running the Game

```bash
python main.py
```

## Project Structure

```
game/
├── main.py              # Game entry point
├── requirements.txt     # Python dependencies
├── config/              # Configuration files
├── src/
│   ├── core/           # Core game engine
│   ├── entities/       # Game entities (player, NPCs, vehicles)
│   ├── world/          # World generation and map
│   ├── systems/        # Game systems (physics, AI, etc.)
│   ├── ui/             # User interface
│   └── utils/          # Utility functions
├── assets/             # Game assets (sprites, sounds, maps)
└── tests/              # Unit tests
```

## Controls

- **WASD**: Move
- **Mouse**: Look around
- **Space**: Jump/Interact
- **Shift**: Sprint
- **E**: Enter/Exit Vehicle
- **F**: Fire Weapon
- **I**: Open Inventory
- **M**: Open Map
- **ESC**: Menu

## Development Roadmap

1. [x] Project structure setup
2. [ ] Basic player movement and camera
3. [ ] World/map generation
4. [ ] Multiple characters system
5. [ ] Vehicle physics and driving
6. [ ] NPC AI and pathfinding
7. [ ] Combat system
8. [ ] Mission system
9. [ ] Save/Load system
10. [ ] Networking (multiplayer)

## Contributing

Feel free to contribute by submitting issues or pull requests.

## License

Apache License 2.0
