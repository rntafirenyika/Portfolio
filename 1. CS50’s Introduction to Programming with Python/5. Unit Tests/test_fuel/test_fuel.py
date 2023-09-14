#Functions that collectively test implementations of convert and gauge functions from fuel.py.

from fuel import convert, gauge
import pytest

def test_convertNormal():
    assert convert("3/4") == 75
    assert convert("1/3") == 33
    assert convert("2/3") == 67


def test_convertZeroDiv():
    with pytest.raises(ZeroDivisionError):
        assert convert("100/0")

def test_convertValueErr():
    with pytest.raises(ValueError):
        assert convert("three/four")

def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(100) == "F"
    assert gauge(99) == "F"
    assert gauge(25) == "25%"
    assert gauge(75) == "75%"
