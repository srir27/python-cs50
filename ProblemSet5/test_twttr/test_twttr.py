import pytest
from twttr import shorten

def test_shorten_lower():
    assert shorten("twitter") == "twttr"
    assert shorten("bee") == "b"

def test_shorten_upper():
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("BEE") == "B"

def test_shorten_alnum():
    assert shorten("CS50") == "CS50"

def test_shorten_punctuation():
    assert shorten("What's your name?") == "Wht's yr nm?"
