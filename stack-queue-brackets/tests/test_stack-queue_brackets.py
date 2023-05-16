import pytest
from stack_queue_brackets import validate_brackets

def test_validate_brackets():
    assert validate_brackets("") == True
    assert validate_brackets("()") == True
    assert validate_brackets("()[]{}") == True
    assert validate_brackets("(]") == False
    assert validate_brackets("([)]") == False
    assert validate_brackets("{[]}") == True
    assert validate_brackets("[") == False
    assert validate_brackets("]") == False
    assert validate_brackets("{{[[(())]]}}") == True
