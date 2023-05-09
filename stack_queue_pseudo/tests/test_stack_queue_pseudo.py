import pytest
from stack_queue_pseud import PseudoQueue

def test_1():
    tester=PseudoQueue()
    tester.enqueue("1")
    tester.enqueue("2")
    tester.enqueue("3")
    tester.enqueue("4")
    tester.enqueue("5")
    actual=tester.dequeue()
    expected="1"
    assert actual==expected

def test_2():
    tester=PseudoQueue()
    tester.enqueue("1")
    tester.enqueue("2")
    tester.enqueue("3")
    tester.enqueue("4")
    tester.enqueue("5")
    tester.dequeue()
    tester.dequeue()
    actual=tester.enqueue("7")
    expected="7 --> 5 --> 4 --> 3 --> None"
    assert actual==expected    

def test_3():
   tester=PseudoQueue()
   tester.enqueue("1")
   tester.enqueue("2")
   tester.enqueue("3")
   tester.enqueue("4")   
   actual=tester.enqueue("5")
   expected="5 --> 4 --> 3 --> 2 --> 1 --> None"
   assert actual == expected