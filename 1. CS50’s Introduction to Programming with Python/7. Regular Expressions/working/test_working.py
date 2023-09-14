from working import convert
import pytest

def test_normal():
    assert convert('9 AM to 5 PM') == '09:00 to 17:00'

def test_normalWithMins():
    assert convert('9:00 AM to 5:00 PM') == '09:00 to 17:00'
    assert convert('10:30 PM to 8:50 AM') == '22:30 to 08:50'

def test_nightShift():
    assert convert('10 PM to 8 AM') == '22:00 to 08:00'

def test_InvalidHours():
    with pytest.raises(ValueError):
        assert convert('13:10 AM to 17:00 PM')

def test_InvalidMins():
    with pytest.raises(ValueError):
        assert convert('9:60 AM to 5:60 PM')

def test_InvalidTo():
    with pytest.raises(ValueError):
        assert convert('9 AM - 5 PM')

def test_InvalidChar():
    with pytest.raises(ValueError):
        assert convert('09:00 AM - 17:00 PM')