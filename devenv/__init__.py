"""Initialize some globals"""
from appdirs import user_config_dir

DEVENV_DIR: str = user_config_dir("devenv")
SCRIPTS_DIR: str = f"{DEVENV_DIR}/scripts"
VERSION: str = "v0.1"
