import pytest
from string_calculator import add

def test_empty_string_returns_zero():
    assert add("") == 0

def test_newline_delimiter():
    assert add("1\n2,3") == 6

def test_custom_delimiter():
    assert add("//;\n1;2") == 3

def test_ignore_larger_numbers():
    assert add("2, 1001") == 2

def test_negative_numbers_not_allowed():
    with pytest.raises(ValueError, match="negative numbers not allowed: -2,-3"):
        add("1,-2,3,-3")

def test_single_number():
    assert add("1") == 1
    assert add("5") == 5

def test_two_numbers():
    assert add("1,2") == 3

def test_multiple_numbers():
    assert add("1,2,3") == 6
    assert add("4,5,6,7") == 22

def test_multiple_delimiters():
    assert add("//[*][%]\n1*2%3") == 6

def test_multiple_delimiters_with_different_lengths():
    assert add("//[**][%%]\n1**2%%3") == 6