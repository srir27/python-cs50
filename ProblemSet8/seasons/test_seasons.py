import pytest
from datetime import date, timedelta
from seasons import date_mins, num_to_words


def test_date_mins():
    # Today should be 0 minutes old
    today = date.today().isoformat()
    assert date_mins(today) == 0

    # Yesterday should be exactly 1 day = 1440 minutes
    yesterday = (date.today() - timedelta(days=1)).isoformat()
    assert date_mins(yesterday) == 1440

    # Leap-year date
    dob = "2020-02-29"
    expected = (date.today() - date(2020, 2, 29)).days * 24 * 60
    assert date_mins(dob) == expected


def test_invalid_dates():
    # Wrong formats
    with pytest.raises(SystemExit):
        date_mins("January 1, 2000")

    with pytest.raises(SystemExit):
        date_mins("01-01-2000")

    with pytest.raises(SystemExit):
        date_mins("2000/01/01")

    # Impossible dates
    with pytest.raises(SystemExit):
        date_mins("2000-02-30")

    with pytest.raises(SystemExit):
        date_mins("2000-13-01")

    with pytest.raises(SystemExit):
        date_mins("2000-00-01")

    # Future date
    with pytest.raises(SystemExit):
        date_mins("2099-01-01")


def test_num_to_words():
    assert num_to_words(0) == "Zero minutes"
    assert num_to_words(1) == "One minutes"
    assert num_to_words(60) == "Sixty minutes"
    assert num_to_words(123) == "One hundred twenty-three minutes"
    assert num_to_words(525600) == "Five hundred twenty-five thousand, six hundred minutes"
    assert num_to_words(1440000) == "One million, four hundred forty thousand minutes"
