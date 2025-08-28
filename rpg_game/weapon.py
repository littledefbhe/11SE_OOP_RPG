from typing import Dict, List, Optional
import random
from inventory import Item
from constants import (
    WEAPON_ROCK_NAME, WEAPON_ROCK_DAMAGE_BONUS, WEAPON_ROCK_DESCRIPTION,
    WEAPON_PAPER_NAME, WEAPON_PAPER_DAMAGE_BONUS, WEAPON_PAPER_DESCRIPTION,
    WEAPON_SCISSORS_NAME, WEAPON_SCISSORS_DAMAGE_BONUS, WEAPON_SCISSORS_DESCRIPTION,
    WEAPON_DAGGER_NAME, WEAPON_DAGGER_DAMAGE_BONUS, WEAPON_DAGGER_DESCRIPTION,
    WEAPON_STAFF_NAME, WEAPON_STAFF_DAMAGE_BONUS, WEAPON_STAFF_DESCRIPTION,
    BOSS_WEAPON_NAME, BOSS_WEAPON_DAMAGE_BONUS, BOSS_WEAPON_DESCRIPTION
)

class Weapon(Item):
    """Weapon items that provide damage bonus."""
    def __init__(self, name: str, description: str, damage_bonus: int):
        """
        Initialize a weapon with a name, description, and damage bonus.
        
        Args:
            name: Weapon's name
            description: Weapon's description
            damage_bonus: Damage bonus provided by the weapon
        """
        super().__init__(name, description)
        self.damage_bonus = damage_bonus

# Update WEAPON_FACTORY with new weapon definitions
WEAPON_FACTORY = {
    WEAPON_ROCK_NAME: lambda: Weapon(WEAPON_ROCK_NAME, WEAPON_ROCK_DESCRIPTION, WEAPON_ROCK_DAMAGE_BONUS),
    WEAPON_PAPER_NAME: lambda: Weapon(WEAPON_PAPER_NAME, WEAPON_PAPER_DESCRIPTION, WEAPON_PAPER_DAMAGE_BONUS),
    WEAPON_SCISSORS_NAME: lambda: Weapon(WEAPON_SCISSORS_NAME, WEAPON_SCISSORS_DESCRIPTION, WEAPON_SCISSORS_DAMAGE_BONUS),
    WEAPON_DAGGER_NAME: lambda: Weapon(WEAPON_DAGGER_NAME, WEAPON_DAGGER_DESCRIPTION, WEAPON_DAGGER_DAMAGE_BONUS),
    WEAPON_STAFF_NAME: lambda: Weapon(WEAPON_STAFF_NAME, WEAPON_STAFF_DESCRIPTION, WEAPON_STAFF_DAMAGE_BONUS),
    BOSS_WEAPON_NAME: lambda: Weapon(BOSS_WEAPON_NAME, BOSS_WEAPON_DESCRIPTION, BOSS_WEAPON_DAMAGE_BONUS)
}

class RockWeapon(Weapon):
    """Rock weapon with moderate damage."""
    def __init__(self):
        super().__init__(WEAPON_ROCK_NAME, WEAPON_ROCK_DESCRIPTION, WEAPON_ROCK_DAMAGE_BONUS)

class PaperWeapon(Weapon):
    """Paper weapon with balanced damage."""
    def __init__(self):
        super().__init__(WEAPON_PAPER_NAME, WEAPON_PAPER_DESCRIPTION, WEAPON_PAPER_DAMAGE_BONUS)

class ScissorsWeapon(Weapon):
    """Scissors weapon with high damage."""
    def __init__(self):
        super().__init__(WEAPON_SCISSORS_NAME, WEAPON_SCISSORS_DESCRIPTION, WEAPON_SCISSORS_DAMAGE_BONUS)

class DaggerWeapon(Weapon):
    """Dagger weapon with high damage."""
    def __init__(self):
        super().__init__(WEAPON_DAGGER_NAME, WEAPON_DAGGER_DESCRIPTION, WEAPON_DAGGER_DAMAGE_BONUS)

class StaffWeapon(Weapon):
    """Staff weapon with magical damage."""
    def __init__(self):
        super().__init__(WEAPON_STAFF_NAME, WEAPON_STAFF_DESCRIPTION, WEAPON_STAFF_DAMAGE_BONUS)

class BossWeapon(Weapon):
    """Special weapon for bosses with enhanced damage."""
    def __init__(self):
        super().__init__("Boss Weapon", 5)

WEAPON_FACTORY = {
    "Rock": RockWeapon,
    "Paper": PaperWeapon,
    "Scissors": ScissorsWeapon
}
