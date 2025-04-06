"""Utility functions for working with the shell, such as handling keyboard interrupts, errors, and
colors, as well as reading and writing files.
"""

from __future__ import annotations

import os
import subprocess
import sys
from typing import TYPE_CHECKING, TypeVar

from textparse import color

if TYPE_CHECKING:
    from textparse.types import ColorName

T = TypeVar("T")


def is_root_user() -> bool:
    """Confirm that the script is running as root.

    Returns:
        Whether the script is running as root.
    """
    return False if sys.platform.startswith("win") else os.geteuid() == 0


def acquire_sudo() -> bool:
    """Acquire sudo access.

    Returns:
        Whether sudo access was successfully acquired.
    """
    try:  # Check if we already have sudo privileges
        subprocess.run(
            ["sudo", "-n", "true"],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        return True
    except subprocess.CalledProcessError:
        try:  # If we don't have sudo privileges, try to acquire them
            subprocess.run(["sudo", "-v"], check=True)
            return True
        except subprocess.CalledProcessError:
            return False


def get_single_char_input(prompt: str = "") -> str:
    """Read a single character without requiring the Enter key. Mainly for confirmation prompts.
    Supports Windows using msvcrt and Unix-like systems using termios.

    Args:
        prompt: The prompt to display to the user.

    Returns:
        The character that was entered.
    """
    print(prompt, end="", flush=True)

    if sys.platform.startswith("win"):  # Windows-specific implementation
        import msvcrt

        char = msvcrt.getch().decode()  # type: ignore
    else:  # macOS and Linux (adult operating systems)
        import termios
        import tty

        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            char = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return char


def confirm_action(
    prompt: str, default_to_yes: bool = False, prompt_color: ColorName | None = None
) -> bool:
    """Ask the user to confirm an action before proceeding.

    Usage:
        if confirm_action("Do you want to proceed?"):

    Args:
        prompt: The prompt to display to the user.
        default_to_yes: Whether to default to "yes" instead of "no".
        prompt_color: The color of the prompt. Defaults to "white".

    Returns:
        Whether the user confirmed the action.
    """
    options = "[Y/n]" if default_to_yes else "[y/N]"
    full_prompt = color(f"{prompt} {options} ", prompt_color)
    sys.stdout.write(full_prompt)

    char = get_single_char_input("").lower()

    sys.stdout.write(char + "\n")
    sys.stdout.flush()

    return char != "n" if default_to_yes else char == "y"
