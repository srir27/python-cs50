from plates import is_valid

def test_valid():
    assert is_valid("CS50") is True
    assert is_valid("SRN") is True
    assert is_valid("AB") is True
    assert is_valid("ABC123") is True

def test_invalid():
    assert is_valid("CS05") is False
    assert is_valid("ABC000") is False
    assert is_valid("1S50") is False
    assert is_valid("C150") is False
    assert is_valid("12ABC") is False

def test_text_after_num():
    assert is_valid("CS50P") is False

def test_spl_chars():
    assert is_valid("PI3.14") is False

def test_string_size():
    assert is_valid("OUTATIME") is False
    assert is_valid("H") is False

def test_alpha_begin():
    assert is_valid("C5S0") is False
    assert is_valid("55S0") is False




