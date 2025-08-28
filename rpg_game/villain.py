from character import Character
from typing import Optional

class Villain(Character):
    """Base class for regular enemies."""
    def __init__(self, name: str, level: int, health: int, damage: int):
        """
        Initialize a villain with basic stats.
        
        Args:
            name: Villain's name
            level: Villain's level
            health: Initial health points
            damage: Base damage
        """
        super().__init__(name, health, damage)
        self.level = level

    def attack(self, enemy) -> int:
        """
        Attack an enemy character.
        
        Args:
            enemy: The target character to attack
            
        Returns:
            The total damage dealt
        """
        total_damage = self.damage + (self.inventory.equipped_weapon.damage_bonus if self.inventory.equipped_weapon else 0)
        current_health = enemy.get_health()
        effective_defense = enemy.get_effective_defense()
        damage_dealt = max(0, total_damage - effective_defense)
        enemy.set_health(current_health - damage_dealt)
        return damage_dealt

class Goblin(Villain):
    """A small but quick enemy."""
    def __init__(self, level: int):
        super().__init__("Goblin", level, 30 + (5 * level), 5 + level)

    def goblin_attack(self, enemy) -> int:
        """
        Goblin's special attack that has a chance to dodge.
        
        Args:
            enemy: The target character to attack
            
        Returns:
            The damage dealt
        """
        if random.random() < 0.3:  # 30% chance to dodge
            print(f"{self.name} dodged the attack!")
            return 0
        return self.attack(enemy)

class Orc(Villain):
    """A powerful but slow enemy."""
    def __init__(self, level: int):
        super().__init__("Orc", level, 50 + (5 * level), 8 + level)

    def orc_attack(self, enemy) -> int:
        """
        Orc's special attack that has a chance to stun.
        
        Args:
            enemy: The target character to attack
            
        Returns:
            The damage dealt
        """
        if random.random() < 0.2:  # 20% chance to stun
            print(f"{self.name} stunned you!")
        return self.attack(enemy)

class Necromancer(Villain):
    """A magical enemy that can summon skeletons."""
    def __init__(self, level: int):
        super().__init__("Necromancer", level, 40 + (5 * level), 6 + level)

    def summon_skeleton(self) -> Villain:
        """
        Summon a skeleton minion.
        
        Returns:
            A new Skeleton villain
        """
        return Villain("Skeleton", self.level - 1, 20, 4)

    def necromancer_attack(self, enemy) -> int:
        """
        Necromancer's special attack that has a chance to summon a skeleton.
        
        Args:
            enemy: The target character to attack
            
        Returns:
            The damage dealt
        """
        if random.random() < 0.1:  # 10% chance to summon
            skeleton = self.summon_skeleton()
            print(f"{self.name} summoned a skeleton!")
            return skeleton.attack(enemy)
        return self.attack(enemy)
