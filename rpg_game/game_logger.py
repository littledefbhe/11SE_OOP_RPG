"""Module for game logging functionality."""

import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('game.log'),
        logging.StreamHandler()
    ]
)

class GameLogger:
    """Class for handling game logging."""
    def __init__(self):
        """Initialize the logger."""
        self.logger = logging.getLogger(__name__)

    def log(self, message: str, level: str = 'info') -> None:
        """
        Log a message at the specified level.

        Args:
            message: Message to log
            level: Logging level (info, warning, error, debug)
        """
        log_func = getattr(self.logger, level.lower())
        log_func(message)

    def info(self, message: str) -> None:
        """Log an info message."""
        self.log(message)

    def warning(self, message: str) -> None:
        """Log a warning message."""
        self.log(message, 'warning')

    def error(self, message: str) -> None:
        """Log an error message."""
        self.log(message, 'error')

    def debug(self, message: str) -> None:
        """Log a debug message."""
        self.log(message, 'debug')

# Create a singleton instance of GameLogger
logger = GameLogger()
