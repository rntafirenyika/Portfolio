from numb3rs import validate
import pytest

def test_valid():
    assert validate("255.0.0.255") == True

def test_invalidnums():
    assert validate("275.0.0.255") == False

def test_invalidchar():
    assert validate("cat.0.0.255") == False

def test_otherbytes():
    assert validate("220.275.5.27") == False