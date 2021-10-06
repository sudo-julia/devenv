# -*- coding: utf-8 -*-
"""Automate the creation of development environments"""
import argparse
import os
from pathlib import Path
import subprocess
from shutil import Error, copytree
from typing import Dict

from devenv import DEVENV_DIR, SCRIPTS_DIR, VERSION
from devenv.utils import check_dir, confirm, print_error


def copy_scripts(overwrite: bool = False) -> bool:
    """Copies scripts from the devenv installation to the local script directory

    Args:
        overwrite: Overwrite the destination directory if it exists

    Returns:
        bool: True for on successful copy, False if the copy fails
    """
    # TODO: test
    try:
        copytree(Path(__file__).parent / "scripts", DEVENV_DIR, dirs_exist_ok=overwrite)
    except FileExistsError:
        # ask before overwriting
        if confirm(f"'{SCRIPTS_DIR}' already exists. Overwrite? [Y/n] "):
            return copy_scripts(overwrite=True)
    except Error as err:
        print_error(err)
        return False
    return True


def run_scripts(script_dir: Path, lang: str, name: str) -> bool:
    """Runs scripts in a given dir

    Args:
        script_dir: The directory to search for scripts
        lang: The main language of the project
        name: The name of the project

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
    parser.add_argument(
        "--install_scripts", action="store_true", help="install the builtin scripts"
    )
    # parser.add_argument(
    #     "-q", "--quiet", action="store_true", help="supress error messages"
    # )
    parser.add_argument("--version", action="version", version=f"%(prog)s {VERSION}")
    args: argparse.Namespace = parser.parse_args()

    if args.install_scripts:
        if not copy_scripts():
            print_error("Error copying scripts")

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
                    f"Skipping '{directory}', as there are no runnable scripts.",
                    "WARN",
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
