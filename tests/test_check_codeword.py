from lib.check_codeword import *

def test_check_codeword_correct():
    result = check_codeword("horse")
    assert result == "Correct! Come in."

# If codeword is wrong but starts with 'h' and ends with 'e', returns 'Close, but nope.'
def test_check_codeword_start_h_end_e():
    result = check_codeword("have")
    assert result == "Close, but nope."

# If codeword is wrong, starts with 'h' but doesn't end with 'e', returns 'WRONG!'
def test_check_incorrect_codeword_right_first_letter_wrong_last_letter():
    result = check_codeword("health")
    assert result == "WRONG!"

# If codeword is wrong, does not start with 'h' but ends with 'e', returns 'WRONG!
def test_check_incorrect_codeword_wrong_first_letter_right_last_letter():
    result = check_codeword("cheese")
    assert result == "WRONG!"

def test_check_codeword_incorrect():
    result = check_codeword("happy")
    assert result == "WRONG!"

