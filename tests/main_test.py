# -*- coding: utf-8 -*-
import sys
from tempfile import TemporaryDirectory
from unittest.mock import patch

import pytest

from devenv.devenv import main, parse_args


def test_empty_dir():
    # usually we'd use pytest's tmp_path, but it wasn't cleaning up in this instance
    tmpdir = TemporaryDirectory()
    with patch.object(
        sys, "argv", ["devenv", "--scripts_path", tmpdir.name, "python", "devenv"]
    ):
        args = parse_args()
        with pytest.raises(SystemError):
            main(args)
    tmpdir.cleanup()
