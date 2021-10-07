# -*- coding: utf-8 -*-
from io import StringIO

from devenv.devenv import copy_scripts


def test_copy_scripts(monkeypatch, tmp_path):
    main = tmp_path / "main"
    main.mkdir()
    base_scripts = tmp_path / "scripts"
    base_scripts.mkdir()

    assert copy_scripts(base_scripts, main / "scripts") is True

    monkeypatch.setattr("sys.stdin", StringIO("n"))
    assert copy_scripts(base_scripts, main / "scripts") is False

    assert copy_scripts(base_scripts, main / "scripts", overwrite=True) is True

    monkeypatch.setattr("sys.stdin", StringIO("y"))
    assert copy_scripts(base_scripts, main / "scripts") is True
