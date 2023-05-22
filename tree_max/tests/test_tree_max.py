import pytest
from tree_max import Binary_trees

# if the tree is empty
def test_1():
    emp=Binary_trees()
    assert emp.tree_max() == "empty tree"

# if there is only one value
def test_2():
    one=Binary_trees()
    one.adds("15")
    assert one.tree_max()== "15"

# if there is multiple values of numbers
def test_3():
    multi = Binary_trees()
    multi.adds(3)
    multi.adds(18)
    multi.adds(13)
    multi.adds(29)
    multi.adds(-23)
    assert multi.tree_max() == 29
