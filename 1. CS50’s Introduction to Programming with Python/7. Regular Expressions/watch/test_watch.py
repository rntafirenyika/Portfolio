from watch import parse


def test_valid():
    assert parse('<iframe src="http://www.youtube.com/embed/xvFZjo5PgG0"></iframe>') == 'https://youtu.be/xvFZjo5PgG0'

def test_validlong():
    assert parse('<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>') == 'https://youtu.be/xvFZjo5PgG0'

def test_invalidurl():
    assert parse('<iframe width="560" height="315" src="https://cs50.harvard.edu/python"></iframe>') == None

def test_nourl():
    assert parse('This will return no url') == None