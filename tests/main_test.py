# -*- coding: utf-8 -*-
import sys
from unittest.mock import patch
import pytest
from devenv.devenv import main, parse_args


def test_empty_dir(tmp_path):
    with patch.object(
        sys, "argv", ["devenv", "--scripts_path", tmp_path.name, "python", "devenv"]
    ):
        args = parse_args()
        with pytest.raises(SystemError):
            main(args)
