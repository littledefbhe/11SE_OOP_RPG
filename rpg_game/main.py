from game import Game

def main() -> None:
    """Main entry point for the game."""
    game = Game()
    game.show_intro()
    game.setup_game()
    game.handle_boss_battles()

if __name__ == "__main__":
    main()
