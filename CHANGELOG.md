# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2025-05-23]

### Added
- Forked from [Mr-Zamora/11SE_OOP_RPG](https://github.com/Mr-Zamora/11SE_OOP_RPG.git)

## [Unreleased]

### Added
- Initial project setup and structure
- Basic README with project information
- CHANGELOG.md for tracking changes
- New modular file structure:
  - `main.py`: Main entry point with game initialization
  - `utilities.py`: Console utility functions (clear_screen, press_enter, print_border)
  - `weapon.py`: Weapon class implementation with factory pattern
  - `character.py`: Character class with encapsulation
  - `boss.py`: Boss class inheriting from Character
  - `game.py`: Game logic and state management
  - `game_logger.py`: Game logging functionality
  - `constants.py`: Centralized configuration values
  - `game_logger.py`: Game logging functionality
  - `constants.py`: Centralized configuration values
  - Added proper logging throughout the game
  - Added centralized constants for game configuration

### Changed
- Restructured codebase to follow OOP principles
- Improved code organization and modularity
- Consolidated utility functions into utilities.py
- Moved weapon constants to weapon.py
- Simplified game.py by removing state pattern
- Improved code maintainability
- Enhanced code readability
- Streamlined game flow implementation
- Made the codebase more modular and maintainable
- Removed redundant files and complexity
- Consolidated constants into appropriate modules
- Simplified module dependencies
- Added proper terminal input handling in utilities.py
- Improved error handling for character name input
- Added automatic continuation for Enter input failures
- Added default values for name and weapon selection
- Fixed Inventory import in character.py
- Added missing weapon constants (Dagger, Staff)
- Fixed weapon initialization in setup_game
- Updated combat system to use get_valid_input
- Improved character stats display
- Fixed health attribute access in game.py
- Updated weapon selection to use correct indices
- Updated weapon factory to use constants
- Added logging throughout the game
- Improved error handling with logging

### Deprecated
- N/A

### Removed
- Removed game_logger.py (moved logging to game.py)
- Removed game_states.py (simplified game flow)
- Removed level_system.py (moved level logic to game.py)
- Removed weapon_types.py (moved to weapon.py)
- Removed redundant type hints and docstrings
- Removed complex timestamp logging
- Removed unnecessary circular dependencies
- Removed duplicate setup_game methods
- Removed redundant weapon selection prompts

### Fixed
- Fixed terminal input handling to prevent EOF errors
- Fixed game flow to handle automatic continuation
- Fixed default value handling for character name and weapon selection
- Fixed NameError with missing Inventory import
- Fixed KeyError with missing weapon constants
- Fixed TypeError with missing damage_bonus parameter
- Fixed AttributeError with incorrect health attribute access
- Fixed combat system to handle non-interactive mode

### Security
- N/A

## Status Against ROADMAP Requirements

✅ **Goals**:
- [x] Keep the code organized in a simple, flat structure
- [x] Maintain clear separation of concerns
- [x] Make it easy to understand and modify
- [x] Focus on demonstrating OOP concepts

✅ **Implementation Approach**:
- [x] Clean, flat file structure
- [x] Clear separation of concerns
- [x] Easy to understand and modify
- [x] Focus on OOP concepts

✅ **Implementation Steps**:
1. [x] Created file structure as outlined
2. [x] Extracted utility functions to utilities.py
3. [x] Extracted game entities (Weapon, Character, Boss)
4. [x] Extracted game logic to game.py
5. [x] Created entry point in main.py

✅ **Core OOP Concepts**:
- [x] Encapsulation (Character class with private attributes)
- [x] Composition (Character contains Weapon)
- [x] Inheritance (Boss inherits from Character)
- [x] Method overriding (Boss.attack())
- [x] Use of super()

✅ **Code Organization**:
- [x] Clear file structure
- [x] Separation of concerns
- [x] Modularity
- [x] Scalability
- [x] Collaboration-friendly structure
- [x] Encapsulation and abstraction

✅ **Constants Management**:
- [x] Centralized constants in constants.py
- [x] Weapon constants
- [x] Boss constants
- [x] Character stats
- [x] Game settings

❌ **Missing Features**:
- [ ] UML class diagram needs to be created
- [ ] README.md needs to be updated with usage instructions
- [ ] More comprehensive testing needed
- [ ] Additional game features (items, levels) could be added

Next Steps:
1. Create UML class diagram
2. Update README.md
3. Add more comprehensive testing
4. Consider adding additional game features
5. Polish user interface and error handling
6. Add more game modes
