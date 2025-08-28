from character import Character
from boss import Boss, FireBoss, IceBoss
from villain import Villain, Goblin, Orc, Necromancer
from utilities import clear_screen, press_enter, print_border, get_valid_input
from weapon import WEAPON_FACTORY
from constants import (
    PLAYER_START_HEALTH, PLAYER_START_DAMAGE,
    BOSS_START_HEALTH, BOSS_START_DAMAGE,
    DEFAULT_PLAYER_NAME, MAX_HEALTH, MIN_HEALTH,
    MAX_DAMAGE, MIN_DAMAGE, MAX_DEFENSE, MIN_DEFENSE
)
from game_logger import logger
from typing import Optional

class Game:
    """Main game class that manages the game flow."""
    def __init__(self):
        """Initialize the game with bosses and villains."""
        self.current_level = 1
        self.bosses = {
            1: FireBoss(1),
            2: IceBoss(2),
            3: FireBoss(3),
            4: IceBoss(4)
        }
        self.villains = {
            1: [Goblin(1), Orc(1)],
            2: [Goblin(2), Orc(2), Necromancer(2)],
            3: [Goblin(3), Orc(3), Necromancer(3)],
            4: [Goblin(4), Orc(4), Necromancer(4)]
        }
        self.player = None

    def show_intro(self) -> None:
        """Display the game introduction and set up the game.
        
        Design Decisions:
        - Engaging introduction to draw player in
        - Clear game objective
        - Simple player name input
        """
        clear_screen()
        print("Welcome to RPG Adventure!")
        print("In a world where darkness looms, you are the chosen hero")
        print("destined to defeat the evil bosses and restore peace.")
        try:
            name = input("Enter your character's name: ").capitalize()
            if not name:
                name = "Hero"
        except EOFError:
            print("\nUsing default name: Hero")
            name = "Hero"
        self.player = Character(name, 110, 10)
        print_border()
        print(f"Welcome, {name}! Choose your weapon wisely.")
        print_border()
        press_enter()

    def setup_game(self) -> None:
        """Set up the game by initializing the player with a weapon."""
        clear_screen()
        print("Choose your starting weapon:")
        print("1. Rock - A simple rock")
        print("2. Paper - A magical paper")
        print("3. Scissors - Sharp scissors")
        
        choice = get_valid_input("Enter your choice (1-3): ", ["1", "2", "3"])
        
        weapons = [
            WEAPON_FACTORY["Rock"](),
            WEAPON_FACTORY["Paper"](),
            WEAPON_FACTORY["Scissors"]()
        ]
        
        self.player.weapon = weapons[choice]
        print(f"You have chosen the {self.player.weapon.name}!")
        press_enter()

        # Display initial character stats
        print("\nYour character:")
        print(f"Name: {self.player.name}")
        print(f"Health: {self.player._health}")
        print(f"Damage: {self.player.damage} (+{self.player.weapon.damage_bonus} from {self.player.weapon.name})")

    def combat(self, player: Character, enemy: Character) -> bool:
        """
        Handle combat between player and enemy.
        
        Args:
            player: The player character
            enemy: The enemy character
            
        Returns:
            True if player wins, False if enemy wins
        """
        while player.get_health() > 0 and enemy.get_health() > 0:
            print("\n=============> COMBAT <=============")
            print("\nPlayer Stats:")
            print(f"Name: {player.name}")
            print(f"Health: {player.get_health()}")
            print(f"Damage: {player.damage}")
            print(f"Defense: {player.get_effective_defense()}")
            print("\nEquipment:")
            if player.inventory.equipped_weapon:
                print(f"Weapon: {player.inventory.equipped_weapon.name} (+{player.inventory.equipped_weapon.damage_bonus} Damage)")
            else:
                print("Weapon: None")
            if player.inventory.equipped_armor:
                print(f"Armor: {player.inventory.equipped_armor.name} (+{player.inventory.equipped_armor.defense_bonus} Defense)")
            else:
                print("Armor: None")
            
            print("\nEnemy Stats:")
            print(f"Name: {enemy.name}")
            print(f"Health: {enemy.get_health()}")
            print(f"Damage: {enemy.damage}")
            print(f"Defense: {enemy.get_effective_defense()}")
            print("\nEquipment:")
            if enemy.inventory.equipped_weapon:
                print(f"Weapon: {enemy.inventory.equipped_weapon.name} (+{enemy.inventory.equipped_weapon.damage_bonus} Damage)")
            else:
                print("Weapon: None")
            if enemy.inventory.equipped_armor:
                print(f"Armor: {enemy.inventory.equipped_armor.name} (+{enemy.inventory.equipped_armor.defense_bonus} Defense)")
            else:
                print("Armor: None")
            print("====================================")
            
            # Player's turn
            action = get_valid_input("Choose action (attack/use item/equip): ", ["attack", "use item", "equip"])
            
            if action == "0":  # attack
                damage = player.attack(enemy)
                print(f"You dealt {damage} damage to {enemy.name}")
            elif action == "1":  # use item
                item_name = input("Enter item name to use: ").strip()
                result = player.use_item(item_name)
                print(result)
            elif action == "2":  # equip
                item_name = input("Enter item name to equip: ").strip()
                result = player.equip_item(item_name)
                print(result)
            
            # Check if enemy is defeated
            if enemy.get_health() <= 0:
                print(f"\nVictory! You defeated {enemy.name}")
                return True
            
            # Enemy's turn
            print("\nEnemy's turn!")
            if isinstance(enemy, Boss):
                enemy.special_ability()
            damage = enemy.attack(player)
            print(f"{enemy.name} dealt {damage} damage to you")
            
            # Check if player is defeated
            if player.get_health() <= 0:
                print(f"\nDefeat! You were defeated by {enemy.name}")
                return False
        
        return False

    def handle_boss_battles(self) -> None:
        """Handle boss battles until the game ends."""
        while self.current_level <= len(self.bosses):
            print(f"\nYou have entered level {self.current_level}")
            print("First, you must defeat the villains!")
            
            # Fight villains first
            for villain in self.villains[self.current_level]:
                print(f"\nYou face {villain.name}!")
                if not self.combat(self.player, villain):
                    break
            
            # If player is still alive, fight the boss
            if self.player.get_health() > 0:
                print(f"\nYou have defeated all villains! Now face the boss!")
                print(f"Prepare to fight {self.bosses[self.current_level].name}!")
                
                if self.combat(self.player, self.bosses[self.current_level]):
                    self.current_level += 1
                    print(f"\nVictory! You defeated {self.bosses[self.current_level - 1].name}")
                    print(f"You advance to level {self.current_level}")
                else:
                    break
            else:
                break
            
        # Check if game is over
        if self.current_level > len(self.bosses):
            print("\nCongratulations! You have defeated all the bosses!")
        else:
            print("\nGame Over!")

    def end_game(self, victory: bool) -> None:
        """End the game with appropriate message."""
        print_border()
        if victory:
            print("Congratulations! You have defeated all the bosses!")
            print("The realm is now safe from evil forces!")
        else:
            print("Game Over! The evil forces have triumphed...")
            print("Better luck next time!")
        print_border()
        press_enter()

    def get_combat_action(self) -> str:
        """Get player's combat action choice."""
        options = ["attack", "use item", "equip"]
        return get_valid_input("\nChoose action (attack/use item/equip): ", options)

    def use_item(self, player: Character) -> None:
        """Handle item usage in combat."""
        player.display_inventory()
        item_name = input("Enter item name to use (or press Enter to cancel): ").capitalize()
        if item_name:
            result = player.use_item(item_name)
            print(result)

    def equip_item(self, player: Character) -> None:
        """Handle equipment management in combat."""
        player.display_inventory()
        item_type = get_valid_input("\nChoose item type to equip (weapon/armor): ", ["weapon", "armor"])
        
        if item_type == "weapon":
            weapon_name = input("Enter weapon name to equip (or press Enter to cancel): ").capitalize()
            if weapon_name:
                weapon = player.inventory.items.get(weapon_name)
                if isinstance(weapon, Weapon):
                    if player.inventory.equip_weapon(weapon):
                        print(f"Equipped {weapon_name}")
                    else:
                        print("Weapon not found in inventory")
        else:
            armor_name = input("Enter armor name to equip (or press Enter to cancel): ").capitalize()
            if armor_name:
                armor = player.inventory.items.get(armor_name)
                if isinstance(armor, Armor):
                    if player.inventory.equip_armor(armor):
                        print(f"Equipped {armor_name}")
                    else:
                        print("Armor not found in inventory")

    def display_combat_status(self, player: Character, enemy: Character) -> None:
        """Display the current combat status."""
        print("\n=============> COMBAT <=============")
        print("\nPlayer Stats:")
        player.display()
        print("\nEnemy Stats:")
        enemy.display()
        print("====================================")
        press_enter()

    def print_victory_message(self, enemy: Character) -> None:
        """Display victory message."""
        print_border()
        print(f"Victory! You defeated {enemy.name}.")
        print_border()
        press_enter()

    def print_defeat_message(self, enemy: Character) -> None:
        """Display defeat message."""
        print_border()
        print(f"Defeat! You were defeated by {enemy.name}.")
        print_border()
        press_enter()

    def handle_boss_battles(self) -> None:
        """Handle all boss battles in sequence."""
        while self.current_level <= len(self.bosses):
            current_boss = self.bosses[self.current_level]
            print_border()
            print(f"\nYou have entered the lair of the {current_boss.name}.")
            print("He is known for his strength and brutality. Prepare for battle!")
            print_border()
            press_enter()
            
            combat_state = CombatState(current_boss)
            if not combat_state.handle(self):
                break
            
            self.current_level += 1

    def end_game(self, victory: bool) -> None:
        """End the game with appropriate message."""
        print_border()
        if victory:
            print("Congratulations! You have defeated all the bosses!")
            print("The realm is now safe from evil forces!")
        else:
            print("Game Over! The evil forces have triumphed...")
            print("Better luck next time!")
        print_border()
        press_enter()

class CombatState:
    """State for handling combat."""
    def __init__(self, enemy: Character):
        self.enemy = enemy
    
    def handle(self, game: Game) -> bool:
        """Handle combat with the enemy."""
        return game.combat(game.player, self.enemy)
