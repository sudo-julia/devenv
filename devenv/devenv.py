# -*- coding: utf-8 -*-
"""Automate the creation of development environments"""
import argparse
import os
from pathlib import Path
import subprocess
import sys
from typing import Union

from devenv import SCRIPTS_DIR, VERSION


def check_dir(dir_path: Path) -> bool:
    """Check if the a directory exists and has files

    Args:
        lang (str): The language directory to check for

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
    """Collect arguments and run the program"""
    parser: argparse.ArgumentParser = argparse.ArgumentParser(prog="devenv")
    parser.add_argument("lang", help="the language of the project")
    parser.add_argument("name", help="the name of the project")
    parser.add_argument(
        "--install_scripts", action="store_true", help="install the builtin scripts"
    )
    parser.add_argument("--version", action="version", version=f"%(prog)s {VERSION}")
    args: argparse.Namespace = parser.parse_args()

    all_dir: Path = SCRIPTS_DIR / "all"
    lang_dir: Path = SCRIPTS_DIR / args.lang

    try:
        # TODO: clean this up/move to a function
        all_running = check_dir(all_dir)
        lang_running = check_dir(lang_dir)
        dir_statuses = {"all": False, args.lang: False}
        if not all_running and not lang_running:
            print_error(
                f"Cannot run any scripts if '{all_dir}' and '{lang_dir}' are empty!"
            )
            raise SystemExit(1)

        if all_running and not lang_running:
            print_error(
                f"'{lang_dir}' is empty. Add scripts to run for {args.lang} files.",
                "WARN",
            )
            dir_statuses["all"] = True
        elif not all_running and lang_running:
            print_error(
                f"'{all_dir}' is empty. Add scripts to run for all filetypes.", "WARN"
            )
            dir_statuses[args.lang] = True
        else:
            for key in dir_statuses:
                dir_statuses[key] = True

        # TODO: integrate this w above
        for directory in (all_dir, lang_dir):
            if not run_scripts(directory, args.lang, args.name):
                raise SystemExit(1)
    except PermissionError as err:
        raise PermissionError from err


if __name__ == "__main__":
    main()
