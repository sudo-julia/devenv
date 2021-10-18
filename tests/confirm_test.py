# -*- coding: utf-8 -*-
from io import StringIO
from dvnv.utils import confirm


def test_confirm(monkeypatch):
    monkeypatch.setattr("sys.stdin", StringIO("Y\n"))
    assert confirm() is True

    monkeypatch.setattr("sys.stdin", StringIO("f\n"))
    assert confirm() is False
