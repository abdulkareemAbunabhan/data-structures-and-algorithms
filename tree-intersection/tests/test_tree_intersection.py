import pytest
from tree import Tree,Node,TreeNode
from tree_intersection import tree_intersection 
@pytest.fixture
def setup_trees():
    node1 = TreeNode(1)
    node0 = TreeNode(0)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node1.left = node0
    node0.left = node2
    node1.right = node3
    node0.right = node4
    node3.right = node5
    first_tree = Tree()
    first_tree.root = node1
    
    node_2 = TreeNode(2)
    node_5 = TreeNode(5)
    node_10 = TreeNode(10)
    node_20 = TreeNode(20)
    node_10.left = node_5
    node_5.left = node_2
    node_10.right = node_20
    second_tree = Tree()
    second_tree.root = node_10
    
    return first_tree, second_tree

def test_1(setup_trees):
    first_tree, second_tree = setup_trees
    assert [2, 5] == tree_intersection(first_tree, second_tree)

def test_2(setup_trees):
    first_tree, second_tree = setup_trees
    node_15 = TreeNode(15)
    node_5 = TreeNode(5)
    node_2 = TreeNode(2)
    node_20 = TreeNode(20)
    node_10 = TreeNode(10)
    node_15.left = node_5
    node_15.right = node_20
    node_20.left = node_10
    node_10.right=node_2
    third_tree = Tree()
    third_tree.root = node_15
    assert [2,5,20,10] == tree_intersection(second_tree, third_tree)

def test_3(setup_trees):
    first_tree, second_tree = setup_trees
    node_3 = TreeNode(3)
    node_6 = TreeNode(6)
    node_9 = TreeNode(9)
    node_3.left = node_6
    node_3.right = node_9
    fourth_tree = Tree()
    fourth_tree.root = node_3
    assert [3] == tree_intersection(first_tree, fourth_tree)

def test_4(setup_trees):
    first_tree, second_tree = setup_trees
    fifth_tree = Tree()
    assert [] == tree_intersection(first_tree, fifth_tree)

