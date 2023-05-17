import pytest
from stack_queue_brackets import validate_brackets

def test_validate_brackets():
    assert validate_brackets("") == True
    assert validate_brackets("(dlfjs)") == True
    assert validate_brackets("a;skd()[]{}") == True
    assert validate_brackets("(]") == False
    assert validate_brackets("([)]asd") == False
    assert validate_brackets("{[]}") == True
    assert validate_brackets("[asd") == False
    assert validate_brackets("]") == False
    assert validate_brackets("{asd{[[(())]]}}") == True
