# -*- coding: utf-8 -*-
import sys
from tempfile import TemporaryDirectory
from unittest.mock import patch

import pytest

from dvnv.dvnv import main, parse_args


def test_empty_dir():
    # usually we'd use pytest's tmp_path, but it wasn't cleaning up in this instance
    with TemporaryDirectory() as tmpdir:
        with patch.object(
            sys, "argv", ["dvnv", "--scripts_path", tmpdir, "python", "dvnv"]
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
            "dvnv",
            None,
            None,
            "--install_scripts",
            "--scripts_path",
            str(scripts_path),
        ],
    ):
        with pytest.raises(SystemExit):
            main(parse_args())


def test_list_langs_empty_dir(capsys, tmp_path):
    with patch.object(
        sys,
        "argv",
        ["dvnv", None, None, "--scripts_path", str(tmp_path), "--list_langs"],
    ):
        with pytest.raises(SystemExit):
            main(parse_args())
            captured = capsys.readouterr()
            assert (
                captured.stderr
                == f"Return with `--install_scripts` to populate {tmp_path}\n"
            )


def test_list_langs_populated(capsys, tmp_path):
    with patch.object(
        sys,
        "argv",
        ["dvnv", None, None, "--scripts_path", str(tmp_path), "--list_langs"],
    ):
        with pytest.raises(SystemExit):
            for lang in ("all", "python", "vim"):
                (tmp_path / lang).mkdir()
            main(parse_args())
            captured = capsys.readouterr()
            assert captured.stdout == "Available languages are:  all python vim\n"


def test_permission_error(tmp_path):
    scripts_path = tmp_path / "scripts"
    scripts_path.mkdir(0o000)
    with patch.object(
        sys,
        "argv",
        ["dvnv", "python", "test-proj", "--scripts_path", str(scripts_path)],
    ):
        with pytest.raises(PermissionError):
            main(parse_args())
    # add all permissions back so the directory can be cleaned up
    scripts_path.chmod(0o777)
