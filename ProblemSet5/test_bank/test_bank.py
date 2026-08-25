from bank import value
def test_hello():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("HELLO") == 0
    assert value("hello, world") == 0


def test_h():
    assert value("hi") == 20
    assert value("Hi") == 20
    assert value("How are you?") == 20


def test_other():
    assert value("What's happening?") == 100
    assert value("good morning") == 100
    assert value("") == 100