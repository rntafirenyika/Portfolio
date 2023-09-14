#Test implementation of shorten function from twttr.py.

from twttr import shorten

def test_twttr():
    assert shorten("THE MAN IS TALL") == "TH MN S TLL"
    assert shorten("the man is tall") == "th mn s tll"
    assert shorten("ThE man IS Tall") == "Th mn S Tll"
    assert shorten("CS50") == "CS50"
    assert shorten("What's your name?") == "Wht's yr nm?"