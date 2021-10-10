#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path
import sys


def main():
    proj_name = sys.argv[2]
    proj_path = Path(proj_name)
    # make the project directory
    if not proj_path.exists():
        proj_path.mkdir(parents=True)
    # create tests and src dirs
    for direc in (proj_name.replace("-", "_"), "tests"):
        new_dir = proj_path / direc
        new_dir.mkdir()
        (new_dir / "__init__.py").touch()
    # create README
    (proj_path / "README.md").touch()


if __name__ == "__main__":
    main()
