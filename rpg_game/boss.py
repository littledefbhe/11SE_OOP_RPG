"""Module containing the Boss class and related functionality.

Design Decisions:
- Boss class extends Character to provide special abilities
- Distinct boss types with unique mechanics
- Special abilities add strategic depth
"""

from character import Character
from weapon import Weapon
from typing import Optional
import random

class Boss(Character):
    """Base class for boss enemies.
    
    Design Decisions:
    - Inheritance from Character provides base functionality
    - Special abilities distinguish bosses from regular enemies
    - Level scaling ensures difficulty progression
    """
    def __init__(self, name: str, level: int, health: int, damage: int):
        """
        Initialize a boss with enhanced stats.
        
        Design Decisions:
        - Bosses have higher stats than regular enemies
        - Level scaling ensures difficulty progression
        - Special weapons provide unique combat mechanics
        """
        super().__init__(name, health, damage)
        self.level = level
        
        # Add and equip boss weapon
        boss_weapon = Weapon("Boss Weapon", "A powerful weapon", 5)
        self.inventory.add_item(boss_weapon)
        self.inventory.equip_weapon(boss_weapon)

    def special_ability(self) -> None:
        """Base special ability method.
        
        Design Decisions:
        - Abstract method for boss-specific abilities
        - Ensures all bosses have unique mechanics
        """
        pass

class FireBoss(Boss):
    """A boss that uses fire-based attacks.
    
    Design Decisions:
    - Fire-based mechanics add variety to combat
    - Area-of-effect damage creates strategic positioning
    - Higher damage output for boss status
    """
    def __init__(self, level: int):
        super().__init__("Fire Boss", level, 80 + (10 * level), 12 + level)

    def fire_attack(self, enemy) -> int:
        """
        Fire-based attack that deals extra damage.
        
        Design Decisions:
        - Additional damage represents fire effect
        - Random damage adds unpredictability
        - Clear feedback about fire damage
        """
        base_damage = self.attack(enemy)
        fire_damage = random.randint(5, 10)
        print(f"{self.name} burns you with fire! Extra {fire_damage} damage!")
        enemy.take_damage(fire_damage)
        return base_damage + fire_damage

    def special_ability(self) -> None:
        """Fire boss's special ability - Firestorm.
        
        Design Decisions:
        - Signature ability for boss identification
        - Creates dramatic combat moments
        """
        print(f"{self.name} unleashes a Firestorm!")

class IceBoss(Boss):
    """A boss that uses ice-based attacks.
    
    Design Decisions:
    - Ice mechanics add strategic depth
    - Status effects create gameplay variety
    - Balanced stats for challenging combat
    """
    def __init__(self, level: int):
        super().__init__("Ice Boss", level, 90 + (10 * level), 10 + level)

    def ice_attack(self, enemy) -> int:
        """
        Ice-based attack that reduces enemy's speed.
        
        Design Decisions:
        - Status effect adds strategic element
        - Probability-based effect maintains balance
        - Clear feedback about status changes
        """
        base_damage = self.attack(enemy)
        if random.random() < 0.3:  # 30% chance to freeze
            print(f"{self.name} freezes you! Your attacks are slowed!")
        return base_damage

    def special_ability(self) -> None:
        """Ice boss's special ability - Blizzard.
        
        Design Decisions:
        - Signature ability for boss identification
        - Creates dramatic combat moments
        """
        print(f"{self.name} summons a Blizzard!")

    def attack(self, enemy) -> int:
        """
        Enhanced attack method for ice boss.
        
        Design Decisions:
        - Uses specialized attack method
        - Maintains consistent boss behavior
        """
        return self.ice_attack(enemy)
