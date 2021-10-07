# -*- coding: utf-8 -*-
import sys
from unittest.mock import patch

from devenv.devenv import parse_args


def test_parse_args():
    with patch.object(sys, "argv", ["devenv", "python", "devenv"]):
        args = parse_args()
        assert args.lang == "python"
        assert args.name == "devenv"
