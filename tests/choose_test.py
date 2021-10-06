# -*- coding: utf-8 -*-
from io import StringIO
import pytest
from devenv.utils import choose


PROMPT = "Choose between 'a', 'b' or 3: "
OPTIONS = ("a", "b", "3")


def test_choose_correct(monkeypatch):
    monkeypatch.setattr("sys.stdin", StringIO("a\n"))
    assert choose(PROMPT, OPTIONS) == "a"

    monkeypatch.setattr("sys.stdin", StringIO("3\n"))
    assert choose(PROMPT, OPTIONS) == "3"


def test_choose_incorrect(monkeypatch):
    with pytest.raises(EOFError):
        monkeypatch.setattr("sys.stdin", StringIO("2\n"))
        choose(PROMPT, OPTIONS)
