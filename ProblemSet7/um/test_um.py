from um import count

def test_count_chars():
    assert count("um") == 1
    assert count("Um") == 1
    assert count("UM") == 1

def test_count_words():
    assert count("yum, rum, sum") == 0
    assert count("yummy") == 0
    assert count("My name is um, Sam") == 1
    assert count("thermoluminescence") == 0

def test_count_multiple():
    assert count("um, um, um") == 3
    assert count("um... um... um...") == 3
    assert count("um-um-um") == 3
    assert count("um? Um! uM.") == 3
    assert count("um... Um... uM...") == 3
    assert count("um-Um-uM") == 3

def test_invalid_input():
    assert count("123 456") == 0
    assert count("") == 0
