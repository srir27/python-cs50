from jar import Jar
import pytest

def test_init():
    with pytest.raises (ValueError):
        jar = Jar(-2)

    with pytest.raises (ValueError):
        jar = Jar("Ten")

    with pytest.raises (ValueError):
        jar = Jar(10.5)

    jar = Jar(10)
    assert jar.capacity == 10
    assert jar.size == 0

    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(10)
    with pytest.raises(ValueError):
        jar.deposit(45)

    jar = Jar(10)
    with pytest.raises(ValueError):
        jar.deposit(-7)

    jar = Jar()
    jar.deposit(3)
    assert jar.size == 3
    

def test_withdraw():
    jar = Jar(10)
    with pytest.raises(ValueError):
        jar.withdraw(45)

    jar = Jar(10)
    with pytest.raises(ValueError):
        jar.withdraw(-7)

    jar = Jar()
    jar.deposit(3)
    jar.withdraw(1)
    assert jar.size == 2