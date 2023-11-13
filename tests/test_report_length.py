from lib.report_length import *

def test_report_length_one_word():
    result = report_length("hello")
    assert result == f"This string was 5 characters long."

def test_empty_string_report_length():
    result = report_length("")
    assert result == f"This string was 0 characters long."

def test_report_length_multi_words():
    result = report_length("Hello, World!")
    assert result == f"This string was 13 characters long."


def test_report_length_string_of_integers():
    result = report_length("0123456789")
    assert result == f"This string was 10 characters long."

def test_report_length_special_characters():
    result = report_length("!@£$%^")
    assert result == f"This string was 6 characters long."