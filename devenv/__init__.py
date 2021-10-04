"""Initialize some globals"""
from pathlib import Path

from appdirs import user_config_dir

DEVENV_DIR = user_config_dir("devenv")
SCRIPTS_DIR = Path(f"{DEVENV_DIR}/scripts")
VERSION = "v0.1"
