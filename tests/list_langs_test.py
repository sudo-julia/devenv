# -*- coding: utf-8 -*-
from devenv.devenv import list_langs


def test_no_langs(tmp_path):
    # tests searching an empty dir
    assert list_langs(tmp_path) == []

    # tests searching a dir that doesn't exist
    scripts_dir = tmp_path / "scripts"
    assert list_langs(scripts_dir) is None


def test_langs(tmp_path):
    for lang in ("all", "python", "vim"):
        (tmp_path / lang).mkdir()
    assert list_langs(tmp_path) == ["all", "python", "vim"]
