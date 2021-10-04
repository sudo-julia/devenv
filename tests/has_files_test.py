from devenv.devenv import has_files


def test_has_files(tmp_path):
    empty = tmp_path / "empty"
    empty.mkdir()
    assert has_files(empty) is False

    contains_file = tmp_path / "contains_file"
    contains_file.mkdir()
    file = contains_file / "file"
    file.touch()
    assert has_files(contains_file) is True
