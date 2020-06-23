from dsa.challenges.tree_intersection.tree_intersection import tree_intersection
from dsa.data_structures.tree.tree import BinaryTree, Node as TreeNode


def test_tree_intersection():
    tree_1 = BinaryTree()
    tree_1.add(150)
    tree_1.add(100)
    tree_1.add(250)
    tree_1.add(75)
    tree_1.add(160)
    tree_1.add(200)
    tree_1.add(350)
    tree_1.root.left.right.left = TreeNode(125)
    tree_1.root.left.right.right = TreeNode(175)
    tree_1.root.right.right.left = TreeNode(300)
    tree_1.root.right.right.right = TreeNode(500)

    tree_2 = BinaryTree()
    tree_2.add(42)
    tree_2.add(100)
    tree_2.add(600)
    tree_2.add(15)
    tree_2.add(160)
    tree_2.add(200)
    tree_2.add(350)
    tree_2.root.left.right.left = TreeNode(125)
    tree_2.root.left.right.right = TreeNode(175)
    tree_2.root.right.right.left = TreeNode(4)
    tree_2.root.right.right.right = TreeNode(500)

    actural = tree_intersection(tree_1, tree_2)
    expected = [100, 160, 125, 175, 200, 350, 500]
    assert actural == expected
