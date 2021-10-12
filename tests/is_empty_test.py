# -*- coding: utf-8 -*-
from pathlib import Path
from tempfile import TemporaryDirectory

from devenv.utils import is_empty


def test_has_files():
    with TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)
        empty = tmpdir / "empty"
        empty.mkdir()
        assert is_empty(empty) is True

        contains_file = tmpdir / "contains_file"
        contains_file.mkdir()
        file = contains_file / "file"
        file.touch()
        assert is_empty(contains_file) is False
