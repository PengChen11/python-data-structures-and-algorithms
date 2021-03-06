from dsa.data_structures.tree.tree import *

def test_empty_tree():
    assert BinaryTree()


def test_single_root():
    test = BinarySearchTree()
    test.add(1)
    assert test.root.value == 1


def test_left_and_right_single_root():
    test = BinarySearchTree()
    test.add(10)
    test.add(1)
    test.add(20)
    assert test.root.left.value == 1 and test.root.right.value == 20


def test_preOrder():
    test = BinarySearchTree()
    test.add(100)
    test.add(50)
    test.add(200)
    test.add(25)
    test.add(75)
    test.add(155)
    assert test.preOrder() == [100, 50, 25, 75, 200, 155]


def test_inOrder():
    test = BinarySearchTree()
    test.add(100)
    test.add(50)
    test.add(200)
    test.add(25)
    test.add(75)
    test.add(155)
    assert test.inOrder() == [25, 50, 75, 100, 155, 200]


def test_postOrder():
    test = BinarySearchTree()
    test.add(100)
    test.add(50)
    test.add(200)
    test.add(25)
    test.add(75)
    test.add(155)
    assert test.postOrder() == [25, 75, 50, 155, 200, 100]


def test_contains():
    test = BinarySearchTree()
    test.add(100)
    test.add(50)
    test.add(200)
    test.add(25)
    test.add(75)
    test.add(155)
    assert test.contains(200) == True and test.contains(201)==False


def test_breadth_first():
    test = BinaryTree()
    test.add(2)
    test.add(7)
    test.add(5)
    test.add(2)
    test.add(6)
    test.root.right.right=Node(9)
    test.root.left.right.left = Node(5)
    test.root.left.right.right = Node(11)
    test.root.right.right.left=Node(4)

    assert test.preOrder() == [2,7,2,6,5,11,5,9,4]
    assert test.inOrder() == [2,7,5,6,11,2,5,4,9]
    assert test.breadth_first() == [2,7,5,2,6,9,5,11,4]


def test_find_max():
    test = BinaryTree()
    test.add(100)
    test.add(50)
    test.add(200)
    test.add(25)
    test.add(75)
    test.add(155)
    assert test.find_max() == 200
