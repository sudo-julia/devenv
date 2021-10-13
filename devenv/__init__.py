# -*- coding: utf-8 -*-
"""Initialize some globals"""
from pathlib import Path

from appdirs import user_config_dir

DEVENV_DIR: Path = Path(user_config_dir("devenv"))
SCRIPTS_DIR: Path = DEVENV_DIR / "scripts"
VERSION: str = "v0.2.0"
