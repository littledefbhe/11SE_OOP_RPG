# RPG Game UML Class Diagram

```mermaid
---
title: RPG Game Class Diagram
---
classDiagram
    direction TB

    %% Core Classes
    class Game {
        +setup_game()
        +combat()
        +run()
    }

    class Character {
        -_name: str
        -_health: int
        -_damage: int
        -_defense: int
        -_weapon: Weapon
        -_inventory: Inventory
        +attack(target: Character)
        +take_damage(amount: int)
        +equip_weapon(weapon: Weapon)
        +use_item(item: Item)
    }

    class Boss {
        +attack(target: Character)
    }

    class Weapon {
        -name: str
        -description: str
        -damage_bonus: int
        +__init__(name, description, damage_bonus)
    }

    %% Relationships
    Character "1" -- "1" Weapon: has
    Character "1" -- "1" Inventory: has
    Boss <|-- Character
    Game "1" -- "1" Character: manages
    Game "1" -- "1" Boss: manages

    %% Additional Classes
    class Inventory {
        +add_item(item: Item)
        +remove_item(item: Item)
        +get_items(): List[Item]
    }

    class Item {
        -name: str
        -description: str
        +use(target: Character)
    }

    %% More Specific Weapons
    class RockWeapon {
        +__init__()
    }

    class PaperWeapon {
        +__init__()
    }

    class ScissorsWeapon {
        +__init__()
    }

    class DaggerWeapon {
        +__init__()
    }

    class StaffWeapon {
        +__init__()
    }

    class BossWeapon {
        +__init__()
    }

    %% Weapon Inheritance
    RockWeapon <|-- Weapon
    PaperWeapon <|-- Weapon
    ScissorsWeapon <|-- Weapon
    DaggerWeapon <|-- Weapon
    StaffWeapon <|-- Weapon
    BossWeapon <|-- Weapon

    %% Notes
    note right of Character
        Base class for all characters
        Demonstrates encapsulation
        Contains Weapon through composition
    end note

    note right of Boss
        Inherits from Character
        Overrides attack method
        Demonstrates inheritance and polymorphism
    end note

    note right of Weapon
        Base class for all weapons
        Used by Character through composition
    end note

    note right of Game
        Manages game flow
        Coordinates between entities
        Demonstrates class relationships
    end note
```
