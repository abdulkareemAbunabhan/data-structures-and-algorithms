import pytest
from stack_queue_animal_sheltr import AnimalShelter
from Node import Node

def test_empty():#tests if can create empty queue
    emp=AnimalShelter()
    actual=emp.shelter.__str__()
    expected="Empty queue"
    assert actual == expected

def test_enqueue(): #tests enqueue method
    ink=AnimalShelter()
    node=Node("catty","cat")
    ink.enqueue(node)
    actual=(ink.shelter.__str__())
    expected="cat -->  None"
    assert actual == expected

def test_dequeue():#tests dequeue from method
    excl=AnimalShelter()
    node=Node("danger","dog")
    ashgar=Node("ashgar","cat")
    asmar=Node("asmar","dog")
    rexy=Node("rexy","cat")
    excl.enqueue(rexy)
    excl.enqueue(asmar)
    excl.enqueue(ashgar)
    excl.enqueue(node)
    actual=excl.dequeue("dog")
    expected={'name': 'asmar', 'species': 'dog'}
    assert actual == expected

def test_dequeue_without_pref():#this test is for the strech goal and will test if the dequeue from the queue without providg q pref will return the first elment or not
    strch=AnimalShelter()
    node=Node("danger","dog")
    ashgar=Node("ashgar","cat")
    asmar=Node("asmar","dog")
    rexy=Node("rexy","cat")
    strch.enqueue(rexy)
    strch.enqueue(asmar)
    strch.enqueue(ashgar)
    strch.enqueue(node)
    actual=strch.dequeue()
    expected={"name":"rexy","species":"cat"}
    assert actual == expected
   
def test_dequeue_onEmpty(): #this test for testing if dequeue from empty queue will raise an Exception
    with pytest.raises(Exception):
     emp=AnimalShelter()
     emp.dequeue()