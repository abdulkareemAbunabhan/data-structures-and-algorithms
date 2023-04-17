import pytest
from linked_list import Linked_list

def test_add():
   ll=Linked_list()
   ll.append("d")
   excepted = 'd -->  None'
   actual = str(ll)
   assert actual == excepted

def test_add():
   ll=Linked_list()
   ll.append("c")
   ll.append("d")
   excepted = 'c --> d -->  None'
   actual = str(ll)
   assert actual == excepted   

def test_before():
   ll=Linked_list()
   ll.append("a")
   ll.append("b")
   ll.insert_before("b","v")
   excepted = 'a --> v --> b -->  None'
   actual = str(ll)
   assert actual == excepted

def test_before1():
   ll=Linked_list()
   ll.append("a")
   ll.append("b")
   ll.insert_before("a","v")
   excepted = 'v --> a --> b -->  None'
   actual = str(ll)
   assert actual == excepted

def test_after():
   ll=Linked_list()
   ll.append("a")
   ll.append("b")
   ll.insert_after("a","v")
   excepted = 'a --> v --> b -->  None'
   actual = str(ll)
   assert actual == excepted

def test_after1():
   ll=Linked_list()
   ll.append("a")
   ll.append("b")
   ll.insert_after("b","v")
   excepted = 'a --> b --> v -->  None'
   actual = str(ll)
   assert actual == excepted
#########################################     delete tests    ####################################

def test_delete():
    ll=Linked_list()
    excepted=False
    actual=ll.delete_node("a")
    assert actual == excepted

def test_delete1():
    ll=Linked_list()
    ll.append("a")
    ll.append("b")
    ll.delete_node("a")
    excepted='b -->  None'
    actual=str(ll)
    assert actual == excepted

def test_delete2():
    ll=Linked_list()
    ll.append("a")
    ll.append("b")
    ll.append("c")
    ll.delete_node("b")
    excepted='a --> c -->  None'
    actual=str(ll)
    assert actual == excepted    

def test_10():
    ll=Linked_list()
    ll.append("a")
    ll.append("b")
    ll.append("c")  
    excepted=False
    actual=ll.delete_node("e")
    assert actual == excepted
##########################################       fixtures     ###################################################
@pytest.fixture
def ll():
    ll = Linked_list()
    ll.insert("D") 
    ll.insert("A") 
    ll.insert("D") 
    return ll