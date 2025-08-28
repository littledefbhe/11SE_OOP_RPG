"""Module containing item definitions and constants."""

from typing import Dict

class Item:
    """Base class for all items in the game."""
    def __init__(self, name: str, description: str, effect: Dict[str, int]):
        self.name = name
        self.description = description
        self.effect = effect

class HealingPotion(Item):
    """A potion that restores health."""
    def __init__(self):
        super().__init__(
            "Healing Potion",
            "A potion that restores 20 health points.",
            {"health": 20}
        )

class FireballScroll(Item):
    """A scroll that casts a powerful fireball spell."""
    def __init__(self):
        super().__init__(
            "Fireball Scroll",
            "A scroll that casts a powerful fireball spell, dealing 15 damage.",
            {"damage": 15}
        )

class LeatherArmor(Item):
    """Light armor that provides basic protection."""
    def __init__(self):
        super().__init__(
            "Leather Armor",
            "Light armor that provides basic protection, increasing defense by 5.",
            {"defense": 5}
        )

# Predefined items
HEALING_POTION = HealingPotion()
FIREBALL_SCROLL = FireballScroll()
LEATHER_ARMOR = LeatherArmor()
