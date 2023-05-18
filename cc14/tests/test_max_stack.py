import pytest
from max_stack import max_stack

def test_1():
    with pytest.raises(Exception):
     dd=max_stack()
     dd.getMax()    
     
def test_2():
    sd=max_stack()
    sd.push(3)
    sd.push(7)
    sd.push(22)
    sd.push(9)
    assert sd.getMax() == 22

def test_3():
   str=max_stack()
   str.push(-11)
   str.push(-23)
   str.push(143)
   assert str.getMax()==143

def test_4():
   negatives=max_stack()
   negatives.push(-11)
   negatives.push(-23)
   negatives.push(-99)
   assert negatives.getMax()==-11