import pytest
from linked_list_kth import Linked_list

def test_kth_first():
    ll= Linked_list()
    actual=ll.linked_list_fromEnd(3)
    expected="Failed"
    assert actual==expected

def test_kth_second():
    ld=Linked_list()
    ld.insert("teste")
    ld.insert("by")
    ld.insert("presented")
    ld.insert("kth")
    actual=ld.linked_list_fromEnd(2)
    excepted="by"
    assert actual==excepted

def test_kth_third():
    la=Linked_list()
    la.insert(1)
    actual=la.linked_list_fromEnd(1)
    expected=1
    assert actual==expected

def test_kth_fourth():
    ld=Linked_list()
    ld.insert(1)
    ld.insert(2)
    ld.insert(3)
    ld.insert(4)
    actual=ld.linked_list_fromEnd(4)
    excepted=4
    assert actual==excepted