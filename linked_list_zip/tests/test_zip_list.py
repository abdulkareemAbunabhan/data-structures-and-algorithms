import pytest
from linked_list import Linked_list
def test_zipLists():
    ll1 = Linked_list()
    ll1.insert(1)
    ll1.insert(2)
    ll1.insert(3)
    ll1.insert(4)
    ####
    ll2 = Linked_list()
    ll2.insert('a')
    ll2.insert('b')
    ll2.insert('c')
    ll2.insert('d')
    actual =str(Linked_list.zipLists(ll1, ll2))
    excepted = "4 ---> d ---> 3 ---> c ---> 2 ---> b ---> 1 ---> a ---> None"
    assert actual == excepted