import pytest
from linked_list import Linked_list, zip_lists

def test_zip_lists_same_length():
    ll1 = Linked_list()
    ll1.insert(1)
    ll1.insert(2)
    ll1.insert(3)

    ll2 = Linked_list()
    ll2.insert(4)
    ll2.insert(5)
    ll2.insert(6)

    zipped_list = zip_lists(ll1, ll2)

    assert zipped_list.__str__() == "3 --> 6 --> 2 --> 5 --> 1 --> 4 -->  None"

def test_zip_lists_different_length():
    ll1 = Linked_list()
    ll1.insert(1)
    ll1.insert(2)

    ll2 = Linked_list()
    ll2.insert(4)
    ll2.insert(5)
    ll2.insert(6)

    zipped_list = zip_lists(ll1, ll2)
    assert zipped_list.__str__() == "2 --> 6 --> 1 --> 5 --> 4 -->  None"

def test_zip_lists_empty_lists():
    ll1 = Linked_list()
    ll2 = Linked_list()
    zipped_list = zip_lists(ll1, ll2)
    assert zipped_list.__str__() == "Empty Linked List"