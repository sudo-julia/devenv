# -*- coding: utf-8 -*-
import sys
from tempfile import TemporaryDirectory
from unittest.mock import patch

import pytest

from devenv.devenv import main, parse_args


def test_empty_dir():
    # usually we'd use pytest's tmp_path, but it wasn't cleaning up in this instance
    with TemporaryDirectory() as tmpdir:
        with patch.object(
            sys, "argv", ["devenv", "--scripts_path", tmpdir, "python", "devenv"]
        ):
            args = parse_args()
            with pytest.raises(SystemError):
                main(args)


def test_install_no_run(tmp_path):
    scripts_path = tmp_path / "scripts"
    with patch.object(
        sys,
        "argv",
        [
            "devenv",
            None,
            None,
            "--install_scripts",
            "--scripts_path",
            str(scripts_path),
        ],
    ):
        with pytest.raises(SystemExit):
            main(parse_args())


def test_permission_error(tmp_path):
    scripts_path = tmp_path / "scripts"
    scripts_path.mkdir(0o000)
    with patch.object(
        sys,
        "argv",
        ["devenv", "python", "test-proj", "--scripts_path", str(scripts_path)],
    ):
        with pytest.raises(PermissionError):
            main(parse_args())
    # add all permissions back so the directory can be cleaned up
    scripts_path.chmod(0o777)
