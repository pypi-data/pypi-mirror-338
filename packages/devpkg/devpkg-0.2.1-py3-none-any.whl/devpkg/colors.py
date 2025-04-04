from __future__ import annotations

from enum import StrEnum


def print_color(text: str, color: str) -> None:
    """Print text in specified color."""
    color_code = getattr(Colors, color.upper(), Colors.RESET)
    print(f"{color_code}{text}{Colors.RESET}")


class Colors(StrEnum):
    """Available types of log formatting."""

    RESET = "\033[0m"
    BOLD = "\033[1m"
    WHITE = "\033[37m"
    BLACK = "\033[30m"
    BLUE = "\033[34m"
    CYAN = "\033[36m"
    GRAY = "\033[90m"
    GREEN = "\033[32m"
    MAGENTA = "\033[95m"
    PURPLE = "\033[35m"
    RED = "\033[31m"
    YELLOW = "\033[33m"
    BRIGHT_BLUE = "\033[94m"
    BRIGHT_CYAN = "\033[96m"
    BRIGHT_GREEN = "\033[92m"
    BRIGHT_RED = "\033[91m"
    BRIGHT_WHITE = "\033[97m"
    BRIGHT_YELLOW = "\033[93m"
