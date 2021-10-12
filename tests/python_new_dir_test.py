# -*- coding: utf-8 -*-
from shutil import rmtree
import sys
from unittest.mock import patch

from scripts.python.new_dir import new_dir


def test_new_dir():
    rmtree("/tmp/new-proj", ignore_errors=True)
    with patch.object(sys, "argv", ["devenv", "python", "/tmp/new-proj"]):
        new_dir()
    rmtree("/tmp/new-proj")
