import pytest
from insertShiftArray import insertShiftArray

def test1():
    actual=insertShiftArray([1,2,3,4,5],3.5)
    expected=[1,2,3,3.5,4,5]
    assert actual == expected

def test2():
    actual=insertShiftArray([1,2,4,5],3.5)
    expected=[1,2,3.5,4,5]
    assert actual == expected

def test3():
    actual=insertShiftArray([],3.5)
    expected=[3.5]
    assert actual == expected    