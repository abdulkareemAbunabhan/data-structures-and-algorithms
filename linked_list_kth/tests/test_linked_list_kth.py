import pytest
from linked_list_kth import Linked_list

def test_kth_first():
    ll= Linked_list()
    actual=ll.linked_list_fromEnd(3)
    expected="Empty"
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


# def test_kth_thid():
#     ls=Linked_list()
#     ls.append("A")
#     ls.append("B")
#     ls.append("D")
#     ls.append("U")
#     ls.append("L")
#     ls.append("K")
#     ls.append("A")
#     ls.append("R")
#     ls.append("E")
#     ls.append("E")
#     ls.append("M")
#     ls.append("1")
#     actual=ls.linked_list_fromEnd(5)
#     expected= "R"
#     assert actual==expected

# def test_kth_fourth():
#     ll= Linked_list()
#     actual=ll.linked_list_fromEnd(0)
#     expected=None
#     assert actual==expected

# def  test_kth_fifth():
#     ld=Linked_list()
#     ld.insert("teste")
#     ld.insert("by")
#     ld.insert("presented")
#     ld.insert("kth")
#     actual=ld.linked_list_fromEnd(22)
#     excepted="Linked list is shorter than u think"
#     assert actual==excepted 

# # def  test_kth_sixth():
# #     ld=Linked_list()
# #     ld.insert("teste")
# #     ld.insert("by")
# #     ld.insert("presented")
# #     ld.insert("kth")
# #     actual=ld.reverser()
# #     excepted="taste --> by --> presented --> kth -->  None"
# #     assert actual==excepted     

# def test_kth_seventh():
#     ls=Linked_list()
#     ls.append("1")
#     ls.append("2")
#     ls.append("3")
#     ls.append("4")
#     ls.append("5")
#     ls.append("6")
#     ls.append("7")
#     ls.append("6")
#     ls.append("5")
#     ls.append("4")
#     ls.append("3")
#     ls.append("2")
#     ls.append("1")
#     actual=ls.isPalindrome()
#     expected= True
#     assert actual==expected

# def test_sad():
#     ls=Linked_list()
#     actual=ls.isPalindrome()
#     expected= "Empty linked list"
#     assert actual==expected

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
