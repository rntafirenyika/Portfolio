from jar import Jar
import pytest

def test_init():
    jar = Jar(15)
    assert jar.capacity == 15
    assert jar.size == 0



def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    with pytest.raises(ValueError):
        assert jar.deposit(14)

    assert jar.deposit(3) == 3

    assert jar.deposit(5) == 8


def test_withdraw():
    jar = Jar()
    assert jar.deposit(3) == 3

    assert jar.withdraw(2) == 1

    with pytest.raises(ValueError):
        assert jar.withdraw(5)