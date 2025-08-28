from typing import Dict, List, Optional
import random

class Item:
    """Base class for all game items."""
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

class Weapon(Item):
    """Weapon items that provide damage bonus."""
    def __init__(self, name: str, description: str, damage_bonus: int):
        super().__init__(name, description)
        self.damage_bonus = damage_bonus

class Armor(Item):
    """Armor items that provide defense bonus."""
    def __init__(self, name: str, description: str, defense_bonus: int):
        super().__init__(name, description)
        self.defense_bonus = defense_bonus

class Consumable(Item):
    """Consumable items that provide temporary effects."""
    def __init__(self, name: str, description: str, effect: str, value: int):
        super().__init__(name, description)
        self.effect = effect
        self.value = value
    
    def use(self, character) -> str:
        """Apply the consumable's effect to the character."""
        if self.effect == "heal":
            character.set_health(character.get_health() + self.value)
            return f"Healed for {self.value} HP"
        elif self.effect == "damage":
            return f"Dealt {self.value} damage"
        return "Consumable used"

class Inventory:
    """Manages a character's items and equipment."""
    def __init__(self, max_size: int = 10):
        self.max_size = max_size
        self.items: Dict[str, Item] = {}
        self.equipped_weapon: Optional[Weapon] = None
        self.equipped_armor: Optional[Armor] = None

    def add_item(self, item: Item) -> bool:
        """
        Add an item to the inventory.
        
        Returns:
            True if item was added, False if inventory is full
        """
        if len(self.items) >= self.max_size:
            return False
        self.items[item.name] = item
        return True

    def remove_item(self, item_name: str) -> Optional[Item]:
        """
        Remove an item from the inventory.
        
        Returns:
            The removed item if found, None otherwise
        """
        return self.items.pop(item_name, None)

    def equip_weapon(self, weapon: Weapon) -> bool:
        """
        Equip a weapon.
        
        Returns:
            True if weapon was equipped, False if not found
        """
        if weapon.name in self.items:
            self.equipped_weapon = weapon
            return True
        return False

    def equip_armor(self, armor: Armor) -> bool:
        """
        Equip armor.
        
        Returns:
            True if armor was equipped, False if not found
        """
        if armor.name in self.items:
            self.equipped_armor = armor
            return True
        return False

    def use_consumable(self, consumable_name: str, character) -> str:
        """
        Use a consumable item.
        
        Returns:
            Message describing the effect
        """
        consumable = self.items.get(consumable_name)
        if isinstance(consumable, Consumable):
            message = consumable.use(character)
            self.remove_item(consumable_name)
            return message
        return "Item not found or not consumable"

    def display_inventory(self) -> None:
        """Display all items in the inventory."""
        print("\nInventory:")
        print("-" * 20)
        for item in self.items.values():
            print(f"{item.name}: {item.description}")
        print("\nEquipped:")
        print("-" * 20)
        print(f"Weapon: {self.equipped_weapon.name if self.equipped_weapon else 'None'}")
        print(f"Armor: {self.equipped_armor.name if self.equipped_armor else 'None'}")

# Predefined items
HEALING_POTION = Consumable(
    "Healing Potion",
    "A potion that restores 20 HP",
    "heal",
    20
)

FIREBALL_SCROLL = Consumable(
    "Fireball Scroll",
    "A scroll that deals 15 damage",
    "damage",
    15
)

LEATHER_ARMOR = Armor(
    "Leather Armor",
    "Light armor that provides moderate defense",
    3
)

IRON_HELMET = Armor(
    "Iron Helmet",
    "Heavy helmet that provides strong defense",
    5
)

# Weapon factory with additional weapons
WEAPON_FACTORY = {
    "Rock": Weapon("Rock", "A simple rock", 2),
    "Paper": Weapon("Paper", "A magical paper", 3),
    "Scissors": Weapon("Scissors", "Sharp scissors", 4),
    "Iron Sword": Weapon("Iron Sword", "A sturdy sword", 6),
    "Magic Staff": Weapon("Magic Staff", "A powerful magical staff", 8)
}
