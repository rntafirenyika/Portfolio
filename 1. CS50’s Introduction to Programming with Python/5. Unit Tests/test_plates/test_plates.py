#Functions that collectively test implementation of is_valid function from plates.py.

from plates import is_valid

def test_normal():
    assert is_valid("CS50") == True
    assert is_valid("ECTO88") == True

def test_numzerostart():
    assert is_valid("CS05") == False
    assert is_valid("CS50P2") == False

def test_nonalphanum():
    assert is_valid("PI3.14") == False

def test_singlechar():
    assert is_valid("H") == False

def test_lotchar():
    assert is_valid("OUTATIME") == False

def test_alphab():
    assert is_valid("A1") == False