# -*- coding: utf-8 -*-
from devenv.devenv import run_scripts

SHEBANG = "#!/usr/bin/env bash"


class TestRunScripts:
    """Tests for run_scripts"""

    def test_non_executable(self, capsys, tmp_path):
        """Assert that a non-executable file will be logged to stderr"""
        script_dir = tmp_path / "scripts"
        script_dir.mkdir(parents=True)
        nonexecutable = script_dir / "nonexecutable"
        with nonexecutable.open("w") as file:
            file.write(f"{SHEBANG}\necho 'hello'")
        assert run_scripts(script_dir, "python", "test") is True
        captured = capsys.readouterr()
        assert captured.err == "[WARN] 'nonexecutable' is not executable! Skipping.\n"

    def test_failure(self, tmp_path):
        """Test case where a command in a script is not found"""
        script_dir = tmp_path / "scripts"
        script_dir.mkdir(parents=True)
        invalid_command = script_dir / "invalid_command"
        with invalid_command.open("w") as file:
            file.write(f"{SHEBANG}\nfake_command")
        invalid_command.chmod(0o111)
        assert run_scripts(script_dir, "python", "test") is False

    def test_success(self, capsys, tmp_path):
        """Test case for success"""
        script_dir = tmp_path / "scripts"
        script_dir.mkdir(parents=True)
        valid_command = script_dir / "hello"
        with valid_command.open("w") as file:
            file.write(f"{SHEBANG}\necho 'hello!'")
        valid_command.chmod(0o777)
        assert run_scripts(script_dir, "python", "test") is True
        captured = capsys.readouterr()
        assert captured.out == "Running 'hello'...\n"
