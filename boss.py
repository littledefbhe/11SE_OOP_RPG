from character import Character
from constants import BOSS_STATS

class Boss(Character):
    """Represents a boss enemy with enhanced stats."""
    def __init__(self, name: str, level: int):
        """
        Initialize a boss with enhanced stats based on level.
        
        Args:
            name: Boss's name
            level: Boss's level (1 or 2)
        """
        stats = BOSS_STATS[name]
        super().__init__(
            name=name,
            health=stats["health"],
            damage=stats["damage"],
            weapon_name=stats["weapon"],
            weapon_damage=stats["weapon_bonus"]
        )
        self.level = level

    def attack(self, enemy) -> int:
        """
        Enhanced attack method for bosses.
        
        Args:
            enemy: The target character to attack
            
        Returns:
            The total damage dealt
        """
        total_damage = super().attack(enemy)
        print(f"{self.name} uses their special ability!")
        return total_damage
