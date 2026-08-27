from working import convert

def test_convert():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("10:30 AM to 2:45 PM") == "10:30 to 14:45"
    assert convert("12 PM to 12 AM") == "12:00 to 00:00"
    assert convert("1 PM to 1 AM") == "13:00 to 01:00"
    assert convert("11:59 PM to 12:01 AM") == "23:59 to 00:01"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("3 PM to 4 PM") == "15:00 to 16:00"
    assert convert("6 AM to 6 PM") == "06:00 to 18:00"