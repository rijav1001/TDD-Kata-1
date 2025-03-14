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