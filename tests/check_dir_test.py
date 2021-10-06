# -*- coding: utf-8 -*-
from devenv.utils import check_dir


def test_check_dir(tmp_path):
    nonexistent = tmp_path / "nonexistent"
    assert check_dir(nonexistent) is False

    empty = tmp_path / "empty"
    empty.mkdir()
    assert check_dir(empty) is False

    working = tmp_path / "working"
    working.mkdir()
    file = working / "file"
    file.touch()
    assert check_dir(working) is True
