# -*- coding: utf-8 -*-
"""utilities that would clutter the main file"""
import sys
from pathlib import Path
from typing import Tuple, Union


def check_dir(dir_path: Path) -> bool:
    """Checks if the a directory exists and has files

    Args:
        dir_path: The directory to check for runnable scripts

    Returns:
        bool: True for success, False otherwise
    """
    if not dir_path.exists() or is_empty(dir_path):
        dir_path.mkdir(parents=True, exist_ok=True)
        print_error(f"Populate '{dir_path}' with scripts!")
        return False
    return True


def choose(prompt: str, options: Tuple) -> str:
    """Returns a value that matches a given option from options

    Args:
        prompt: The prompt to display to the user
        options: A tuple of choices that the user can select from

    Returns:
        str: The string selected from 'options'
    """
    while True:
        option: str = clean_input(prompt)
        if option in options:
            return option
        print("Please choose between: ", *options)


def clean_input(prompt: str) -> str:
    """Returns user input to a prompt, casefolded and stripped of whitespace

    Args:
        prompt: The prompt to display to the user

    Returns:
        str: The user's input to the prompt
    """
    return input(prompt).casefold().strip()


def confirm(prompt: str = None) -> bool:
    """Confirms a choice made by the user

    Args:
        prompt: The prompt to display to the user (default is None)

    Returns:
        bool: True if the user entered 'y' or 'yes', False otherwise
    """
    if not prompt:
        prompt = "Does this information look correct? [Y/n] "
    return clean_input(prompt) in ("y", "yes")


def is_empty(path: Path) -> bool:
    """Checks if a directory has files

    Args:
        path: The path to the directory to check

    Returns:
        bool: True if the dir is empty, False if it contains any files
    """
    return not any(path.iterdir())


def print_error(msg: Union[str, Exception], header: str = "ERR") -> None:
    """Prints a message to stderr

    Args:
        msg: The message to print to stderr
        header: The string to print before the actual message
    """
    print(f"[{header}] {msg}", file=sys.stderr)
