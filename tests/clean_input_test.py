# -*- coding: utf-8 -*-
from io import StringIO
from dvnv.utils import clean_input

PROMPT = "Input: "


def test_clean_input(monkeypatch):
    monkeypatch.setattr("sys.stdin", StringIO("     left SPACE\n"))
    assert clean_input(PROMPT) == "left space"

    monkeypatch.setattr("sys.stdin", StringIO("RIGHT space      \n"))
    assert clean_input(PROMPT) == "right space"

    monkeypatch.setattr("sys.stdin", StringIO("    SURROUNDING SPACE    \n"))
    assert clean_input(PROMPT) == "surrounding space"
