"""MAIN"""
import argparse
import os
from pathlib import Path
import subprocess
import sys

from devenv import SCRIPTS_DIR


def print_error(msg):
    """print a message to stderr"""
    print(f"[ERR] {msg}", file=sys.stderr)


def run_scripts(script_dir, lang, name):
    """run scripts in a given dir"""
    for script in script_dir.iterdir():
        if not os.access(script, os.X_OK):
            print_error(f"{script} is not executable!")
            continue

        try:
            print(f"Running {script}...")
            subprocess.run([str(script.resolve()), lang, name], check=True)
        except subprocess.CalledProcessError as err:
            print_error(err)


def main():
    """:"""
    parser = argparse.ArgumentParser()
    parser.add_argument("lang", help="the language of the project")
    parser.add_argument("name", help="the name of the project")
    args = parser.parse_args()
    lang_dir = Path(f"{SCRIPTS_DIR}/{args.lang}")

    if not lang_dir.exists() and not Path(f"{SCRIPTS_DIR}/all").exists():
        # TODO: check for empty dirs
        print_error(
            f"Please populate '{lang_dir}' and/or '{SCRIPTS_DIR}/all' and run again."
        )
        raise SystemExit(1)

    try:
        for directory in ("/all", f"/{args.lang}"):
            run_scripts(directory, args.lang, args.name)
    except PermissionError as err:
        raise PermissionError from err


if __name__ == "__main__":
    main()
