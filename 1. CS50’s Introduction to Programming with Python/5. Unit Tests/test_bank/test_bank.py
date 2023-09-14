#Functions that collectively test implementation of the value function from bank.py.

from bank import value

def test_default():
    assert value("Hello") == 0

def test_name():
    assert value("Hello, Newman") == 0

def test_hstart():
    assert value("How you doing?") == 20

def test_noh():
    assert value("What's happening?") == 100
    assert value("What's up?") == 100

def test_upper():
    assert value("HELLO") == 0

def test_nums():
    assert value("HELLO CS50") == 0

def test_lower():
    assert value("hello") == 0