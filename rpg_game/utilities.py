import os
from typing import List, Optional

def clear_screen() -> None:
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def press_enter() -> None:
    """Prompt the user to press Enter to continue."""
    try:
        input("\nPress Enter to continue...\n")
    except EOFError:
        print("\nContinuing automatically...")
        return True

def print_border(length: int = 80, char: str = "-") -> None:
    """Print a border for visual separation."""
    print(char * length)

def get_valid_input(prompt: str, options: List[str]) -> int:
    """
    Get valid user input from a list of options.
    
    Args:
        prompt: Input prompt message
        options: List of valid options
        
    Returns:
        Index of the chosen option
    """
    while True:
        try:
            user_input = input(prompt).strip().lower()
            if user_input in options:
                return options.index(user_input)
            print("Invalid input, please try again.")
        except EOFError:
            print("\nUsing default option: attack")
            return 0  # Return first option as default (attack)
