#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Create the base directory"""
from pathlib import Path
from sys import argv


def create_dir():
    """Create the project's base directory"""
    Path(argv[2]).mkdir()


if __name__ == "__main__":
    create_dir()
