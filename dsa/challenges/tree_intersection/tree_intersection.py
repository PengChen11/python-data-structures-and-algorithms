from dsa.data_structures.tree.tree import BinaryTree, Node as TreeNode
from dsa.data_structures.hash_table.hash_table import HashTable
import pysnooper


def tree_intersection(tree1, tree2):
    """function to find the intersection of two binanry trees"""
    new_table = HashTable(100)
    output = []

    def traverse(node, first = False):
        """inner function to traverse inside the tree and check value"""
        if not node:
            return

        if first == True:
            if new_table.contains(node.value) == False:
                new_table.add(node.value,1)

            traverse(node.left, first = True)

            traverse(node.right, first = True)

        else:
            if new_table.contains(node.value):
                output.append(node.value)

            traverse(node.left)
            traverse(node.right)

    traverse(tree1.root, first = True)

    traverse(tree2.root)

    return output


if __name__ == "__main__":

    pass
