import pytest 
from binary_tree import *
# 1- Can successfully instantiate an empty tree
def test_1():
    emp=Binary_trees()
    emp2= Binary_search_tree()
    assert emp.pre_order() == "empty tree"
    assert emp2.in_order() == []
# 2-Can successfully instantiate a tree with a single root node
def test_2():
    single=Binary_trees()
    single2=Binary_search_tree()
    single.adds("1")
    single2.add(1)
    assert single.pre_order()==["1"]
    assert single2.pre_order()==[1]
# 3-For a Binary Search Tree, can successfully add a left child and right child properly to a node
def test_3():
    left_to_right=Binary_search_tree()
    left_to_right.add(5)
    left_to_right.add(3)
    left_to_right.add(7)
    assert left_to_right.in_order()==[3,5,7]   
# 4- Can successfully return a collection from a pre-order traversal
def test_4():
    preTree1=Binary_trees()
    preTree=Binary_search_tree()
    preTree.add(5)
    preTree.add(3)
    preTree.add(7)
    preTree1.adds("5")
    preTree1.adds("3")
    preTree1.adds("7")
    assert preTree.pre_order()==[5,3,7]
    assert preTree1.pre_order()==["5","3","7"]  
# 5- Can successfully return a collection from an in-order traversal
def test_5():
    preTree1=Binary_trees()
    preTree=Binary_search_tree()
    preTree.add(5)
    preTree.add(3)
    preTree.add(7)
    preTree1.adds("5")
    preTree1.adds("3")
    preTree1.adds("7")
    assert preTree.in_order()==[3,5,7]
    assert preTree1.in_order()==["3","5","7"]
# 6- Can successfully return a collection from a post-order traversal
def test_6():
    preTree1=Binary_trees()
    preTree=Binary_search_tree()
    preTree.add(5)
    preTree.add(3)
    preTree.add(7)
    preTree1.adds("5")
    preTree1.adds("3")
    preTree1.adds("7")
    assert preTree.post_order()==[3,7,5]
    assert preTree1.post_order()==["3","7","5"]

# 7- Returns true	false for the contains method, given an existing or non-existing node value
def test_7():
    preTree=Binary_search_tree()
    preTree.add(5)
    preTree.add(3)
    preTree.add(7)
    assert preTree.contains(4)==False
    assert preTree.contains(3)==True
