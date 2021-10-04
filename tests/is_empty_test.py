from devenv.devenv import is_empty


def test_has_files(tmp_path):
    empty = tmp_path / "empty"
    empty.mkdir()
    assert is_empty(empty) is True

    contains_file = tmp_path / "contains_file"
    contains_file.mkdir()
    file = contains_file / "file"
    file.touch()
    assert is_empty(contains_file) is False
