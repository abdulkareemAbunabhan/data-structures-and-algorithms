import pytest
from Stack import Stack

#1 can push on a stack 
def test_one():
    stack1=Stack()
    actual=stack1.push(1)
    expected ="1 -->  None"
    assert actual == expected
# 2 Can successfully push multiple values onto a stack
def test_second():
    stack2=Stack()
    stack2.push("1")
    stack2.push("2")
    stack2.push("3")
    stack2.push("4")
    stack2.push("5")
    actual=stack2.push("D")
    expected= "D --> 5 --> 4 --> 3 --> 2 --> 1 -->  None"
    assert actual==expected
# 7 Calling pop or peek on empty stack raises exception
def test_third():
    with pytest.raises(Exception):
     stack3=Stack()
     stack3.pop()
# 3 Can successfully pop off the stack
def test_fourth():
    stack2=Stack()
    stack2.push("1")
    stack2.push("2")
    stack2.push("3")
    actual=stack2.pop()
    expected= "3"
    assert actual==expected    
# 4 Can successfully empty a stack after multiple pops
def test_fifth():
    stack2=Stack()
    stack2.push("1")
    stack2.push("2")
    stack2.push("3")
    stack2.pop()
    stack2.pop()
    stack2.pop()
    actual=stack2.isEmpty()
    expected= True
    assert actual==expected 
# 5 Can successfully peek the next item on the stack
def test_sixth():
    stack6=Stack()
    stack6.push(1)
    actual=stack6.peek()
    expected=1
    assert actual == expected
# 6 Can successfully instantiate an empty stack
def test_seventh():
    stack7=Stack()
    actual=stack7.__str__()
    expected="Empty stack"
    assert actual == expected 
# 7 Calling pop or peek on empty stack raises exception
def test_eighth():
    with pytest.raises(Exception):
     stack8=Stack()
     stack8.peek()