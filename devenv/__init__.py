# -*- coding: utf-8 -*-
"""Initialize some globals"""
from pathlib import Path

from appdirs import user_config_dir

DEVENV_DIR: str = user_config_dir("devenv")
SCRIPTS_DIR: Path = Path(f"{DEVENV_DIR}/scripts")
VERSION: str = "v0.1.1"
