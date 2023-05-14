import pytest
from Queue import Queue
#  8- Can successfully enqueue into a queue
def test_one():
    queue1=Queue()
    actual=queue1.enqueue(1)
    expected ="1 -->  None"
    assert actual == expected
# 9-Can successfully enqueue multiple values into a queue
def test_second():
    queue2=Queue()
    queue2.enqueue("1")
    queue2.enqueue("2")
    queue2.enqueue("3")
    queue2.enqueue("4")
    queue2.enqueue("5")
    actual=queue2.enqueue("D")
    expected= "1 --> 2 --> 3 --> 4 --> 5 --> D -->  None"
    assert actual==expected
# 14- Calling dequeue or peek on empty queue raises exception
def test_third():
    with pytest.raises(Exception):
     queue3=Queue()
     queue3.dequeue()
# 10-Can successfully dequeue out of a queue the expected value
def test_fourth():
    queue2=Queue()
    queue2.enqueue("1")
    queue2.enqueue("2")
    queue2.enqueue("3")
    actual=queue2.dequeue()
    expected= "1"
    assert actual==expected    
# 12 Can successfully empty a queue after multiple dequeues
def test_fifth():
    queue2=Queue()
    queue2.enqueue("1")
    queue2.enqueue("2")
    queue2.enqueue("3")
    queue2.dequeue()
    queue2.dequeue()
    queue2.dequeue()
    actual=queue2.isEmpty()
    expected= True
    assert actual==expected 
# 11-Can successfully peek into a queue, seeing the expected value
def test_sixth():
    queue6=Queue()
    queue6.enqueue(1)
    actual=queue6.peek()
    expected=1
    assert actual == expected
# 13-Can successfully instantiate an empty queue
def test_seventh():
    queue7=Queue()
    actual=queue7.__str__()
    expected="Empty queue"
    assert actual == expected 
#14-Calling dequeue or peek on empty queue raises exception
def test_eighth():
    with pytest.raises(Exception):
     queue8=Queue()
     queue8.peek()
            