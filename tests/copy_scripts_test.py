# -*- coding: utf-8 -*-
from io import StringIO

from dvnv.dvnv import copy_scripts


def test_copy_scripts(monkeypatch, tmp_path):
    main = tmp_path / "main"
    main.mkdir()
    base_scripts = tmp_path / "scripts"
    base_scripts.mkdir()

    # copy to nonexistent dir
    assert copy_scripts(base_scripts, main / "scripts") is True

    # abort when a dir is in the way
    monkeypatch.setattr("sys.stdin", StringIO("n\n"))
    assert copy_scripts(base_scripts, main / "scripts") is False

    # overwrite an existing dir
    monkeypatch.setattr("sys.stdin", StringIO("y\n"))
    assert copy_scripts(base_scripts, main / "scripts") is True
