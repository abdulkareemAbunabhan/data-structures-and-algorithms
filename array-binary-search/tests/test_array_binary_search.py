import pytest
from array_binary_search import BinarySearch
def test1():
    actual=BinarySearch([1,2,3,4,5,6,7,8],6)
    expected=5
    assert actual==expected

def test2():
    actual=BinarySearch([1,2,3,4,5,6,7,8],9)
    expected=-1
    assert actual==expected

def test3():
    actual=BinarySearch([],3)
    expected=-1
    assert actual==expected