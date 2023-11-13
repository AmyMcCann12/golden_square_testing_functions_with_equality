from lib.greet import *

def test_greet():
    result = greet("Hannah")
    assert result == f"Hello, Hannah!"