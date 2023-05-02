import pytest 
from linked_list import Linked_list

def test_firstTest():
    linkedl=Linked_list()
    linkedl.insert("A")
    actual =linkedl.__str__()
    expected="A -->  None"
    assert actual==expected

def test_search():
    ll=Linked_list()
    ll.insert("A")
    ll.insert("c")
    actual=ll.includes("A")
    expected = True
    assert actual==expected