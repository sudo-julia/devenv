# -*- coding: utf-8 -*-
"""Automate the creation of development environments"""
import argparse
import os
from pathlib import Path
import subprocess
import sys
from typing import Dict, Union

from devenv import SCRIPTS_DIR, VERSION


def check_dir(dir_path: Path) -> bool:
    """Checks if the a directory exists and has files

    Args:
        dir_path (str): The directory to check for runnable scripts

    Returns:
        bool: True for success, False otherwise
    """
    if not dir_path.exists() or is_empty(dir_path):
        dir_path.mkdir(parents=True, exist_ok=True)
        print_error(f"Populate '{dir_path}' with scripts!")
        return False
    return True


def is_empty(path: Path) -> bool:
    """Checks if a directory has files

    Args:
        path (Path): The path to the directory to check

    Returns:
        bool: True if the dir is empty, False if it contains any files
    """
    return not any(path.iterdir())


def print_error(msg: Union[str, Exception], header: str = "ERR") -> None:
    """Prints a message to stderr

    Args:
        msg (str): The message to print to stderr
    """
    print(f"[{header}] {msg}", file=sys.stderr)


def run_scripts(script_dir: Path, lang: str, name: str) -> bool:
    """Runs scripts in a given dir

    Args:
        script_dir (Path): The directory to search for scripts
        lang (str): The main language of the project
        name (str): The name of the project

    Returns:
        bool: True for success, False otherwise
    """
    for script in sorted(script_dir.iterdir()):
        if not os.access(script, os.X_OK):
            print_error(f"'{script.name}' is not executable! Skipping.")
            continue
        if script.is_dir():
            continue

        try:
            print(f"Running '{script.name}'...")
            subprocess.run([str(script.resolve()), lang, name], check=True)
        except subprocess.CalledProcessError as err:
            print_error(f"Error running '{script}'!")
            print_error(err)
            return False
    return True


def main() -> None:
    """Collects arguments and run the program"""
    parser: argparse.ArgumentParser = argparse.ArgumentParser(prog="devenv")
    parser.add_argument("lang", help="the language of the project")
    parser.add_argument("name", help="the name of the project")
    # parser.add_argument(
    #     "--install_scripts", action="store_true", help="install the builtin scripts"
    # )
    parser.add_argument("--version", action="version", version=f"%(prog)s {VERSION}")
    args: argparse.Namespace = parser.parse_args()

    all_dir: Path = SCRIPTS_DIR / "all"
    lang_dir: Path = SCRIPTS_DIR / args.lang
    all_running: bool = check_dir(all_dir)
    lang_running: bool = check_dir(lang_dir)
    script_dirs: Dict[Path, bool] = {all_dir: all_running, lang_dir: lang_running}

    try:
        no_run = 0
        for directory, run in script_dirs.items():
            if not run:
                print_error(
                    f"Skipping '{directory}', as there are no runnable scripts.", "WARN"
                )
                no_run += 1
                continue
            if not run_scripts(directory, args.lang, args.name):
                raise SystemExit(1)
        if no_run == 2:
            print_error(
                f"Did not run any scripts; both '{all_dir}' and '{lang_dir}' are empty!"
            )
    except PermissionError as err:
        raise PermissionError from err


if __name__ == "__main__":
    main()
