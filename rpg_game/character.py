"""Module containing the Character class and related functionality.

Design Decisions:
- Character class serves as the base for all game entities
- Inventory system is integrated for item management
- Health system includes upper and lower bounds for balance
- Equipment system allows for stat customization
"""

from typing import Dict, Optional
import random
from inventory import Inventory
from items import HEALING_POTION, FIREBALL_SCROLL, LEATHER_ARMOR
from weapon import Weapon
from constants import (
    MAX_HEALTH, MIN_HEALTH,
    MAX_DAMAGE, MIN_DAMAGE,
    MAX_DEFENSE, MIN_DEFENSE
)
from game_logger import logger

class Character:
    """Base class for all characters in the game.
    
    Design Decisions:
    - Encapsulates core gameplay mechanics (attack, defense, health)
    - Provides foundation for enemy and player subclasses
    - Manages equipment and inventory through composition
    """
    def __init__(self, name: str, health: int, damage: int):
        """
        Initialize a character with basic attributes.
        
        Design Decisions:
        - Default weapon ensures all characters can attack
        - Inventory initialized for item management
        - Default items provide basic gameplay tools
        """
        self.name = name
        self._health = health
        self.damage = damage
        self.defense = 0
        self.inventory = Inventory()
        self._initialize_default_items()
        
        # Default weapon ensures all characters can attack
        default_weapon = Weapon("Rock", "A simple rock", 2)
        self.inventory.add_item(default_weapon)
        self.inventory.equip_weapon(default_weapon)

    def _initialize_default_items(self) -> None:
        """Initialize default items for new characters.
        
        Design Decisions:
        - Basic healing and offensive options for early game
        - Starter armor for defense
        - Balanced starting equipment for gameplay
        """
        # Default consumables
        self.inventory.add_item(HEALING_POTION)
        self.inventory.add_item(FIREBALL_SCROLL)
        
        # Default armor
        self.inventory.add_item(LEATHER_ARMOR)

    def get_health(self) -> int:
        """Get the current health of the character.
        
        Design Decisions:
        - Health is protected to prevent direct modification
        - Getter method follows encapsulation principle
        """
        return self._health

    def set_health(self, new_health: int) -> None:
        """Set the character's health with bounds checking.
        
        Design Decisions:
        - Health bounds prevent exploits
        - Max health cap ensures game balance
        """
        if new_health < 0:
            self._health = 0
        elif new_health > 1000:  # Max health cap
            self._health = 1000
        else:
            self._health = new_health

    def get_effective_defense(self) -> int:
        """Get the character's total defense including armor.
        
        Design Decisions:
        - Defense calculation includes equipped armor
        - Provides stat stacking for equipment
        """
        return self.defense + (self.inventory.equipped_armor.defense_bonus if self.inventory.equipped_armor else 0)

    def attack(self, enemy) -> int:
        """Attack an enemy character.
        
        Design Decisions:
        - Damage calculation includes equipped weapon
        - Defense system prevents one-hit kills
        """
        total_damage = self.damage + (self.inventory.equipped_weapon.damage_bonus if self.inventory.equipped_weapon else 0)
        current_health = enemy.get_health()
        effective_defense = enemy.get_effective_defense()
        damage_dealt = max(0, total_damage - effective_defense)
        enemy.set_health(current_health - damage_dealt)
        return damage_dealt

    def take_damage(self, damage: int) -> int:
        """Take damage from an attack.
        
        Design Decisions:
        - Uses health setter for consistency
        - Prevents direct modification of health
        """
        effective_defense = self.get_effective_defense()
        actual_damage = max(0, damage - effective_defense)
        self.set_health(self.get_health() - actual_damage)
        return actual_damage

    def use_item(self, item_name: str) -> str:
        """Use a consumable item from inventory.
        
        Design Decisions:
        - Item usage handled through inventory system
        - Provides feedback about item usage
        """
        return self.inventory.use_consumable(item_name, self)

    def display(self) -> None:
        """Display character stats and equipment.
        
        Design Decisions:
        - Shows both base and equipped stats
        - Provides clear equipment status
        """
        print(f"\nName: {self.name}")
        print(f"Health: {self.get_health()}")
        print(f"Damage: {self.damage}")
        print(f"Defense: {self.get_effective_defense()}")
        print("\nEquipment:")
        weapon = self.inventory.equipped_weapon
        armor = self.inventory.equipped_armor
        print(f"Weapon: {weapon.name if weapon else 'None'} (+{weapon.damage_bonus if weapon else 0} Damage)")
        print(f"Armor: {armor.name if armor else 'None'} (+{armor.defense_bonus if armor else 0} Defense)")

    def display_inventory(self) -> None:
        """Display the character's inventory."""
        self.inventory.display_inventory()
