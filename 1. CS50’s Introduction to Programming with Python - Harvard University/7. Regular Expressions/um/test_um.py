from um import count

def test_normal():
    assert count("um, my name is Nashwell") == 1

def test_upper():
    assert count("UM") == 1

def test_WordsWithUm():
    assert count("Um, thanks for the album.") == 1

def test_mixed():
    assert count("Um, thanks, um...") == 2

def test_noUm():
    assert count("word does not exist") == 0