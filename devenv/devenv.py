"""MAIN"""
import argparse
import os
import subprocess
import sys

from devenv import SCRIPTS_DIR


def has_files(path):
    """Checks if a directory has files

    Args:
        path (Path): The path to the directory to check

    Returns:
        bool: True for success, False otherwise
    """
    # TODO: test this
    return bool([file for file in path.iterdir()])


def print_error(msg):
    """Prints a message to stderr

    Args:
        msg (str): The message to print to stderr
    """
    print(f"[ERR] {msg}", file=sys.stderr)


def run_scripts(script_dir, lang, name):
    """Runs scripts in a given dir

    Args:
        script_dir (Path): The directory to search for scripts
        lang (str): The main language of the project
        name (str): The name of the project

    Returns:
        bool: True for success, False otherwise
    """
    for script in script_dir.iterdir():
        if not os.access(script, os.X_OK):
            print_error(f"{script} is not executable!")
            continue
        if script.is_dir():
            continue

        try:
            print(f"Running {script}...")
            subprocess.run([str(script.resolve()), lang, name], check=True)
        except subprocess.CalledProcessError as err:
            print_error(err)


def main():
    """Collect arguments and run the program"""
    parser = argparse.ArgumentParser()
    parser.add_argument("lang", help="the language of the project")
    parser.add_argument("name", help="the name of the project")
    args = parser.parse_args()

    all_dir = SCRIPTS_DIR / "all"
    lang_dir = SCRIPTS_DIR / args.lang

    try:
        for directory in (all_dir, lang_dir):
            if not directory.exists() or not has_files(directory):
                print_error(f"Please populate '{directory}' and run again.")
            raise SystemExit(1)
        for directory in (all_dir, lang_dir):
            run_scripts(directory, args.lang, args.name)
    except PermissionError as err:
        raise PermissionError from err


if __name__ == "__main__":
    main()
