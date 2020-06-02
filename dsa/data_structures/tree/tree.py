from collections import deque

class Queue():
    def __init__(self):
        self.storage = deque()

    def enqueue(self, value):
        self.storage.appendleft(value)

    def dequeue(self):
        return self.storage.pop()

    def peek(self):
        return self.storage[-1]

    def is_empty(self):
        return len(self.storage) == 0

class Node:
    def __init__(self,value,left=None,right=None):
        self.value = value
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self):
        self.root = None

    def preOrder(self):
        """pre-order method"""
        output = []
        def traverse(node):
            """inner function to append the right value to output list"""
            if not node:
                return
            output.append(node.value)
            traverse(node.left)
            traverse(node.right)
        traverse(self.root)

        return output

    def inOrder(self):
        """in-order traversal method"""
        output = []
        def traverse(node):
            """inner recursion function to append the right value to output list"""
            if not node:
                return

            if not node.left and not node.right:
                output.append(node.value)
                return
            else:
                traverse(node.left)

            output.append(node.value)
            if not node.right and not node.left:
                output.append(node.value)
                return
            else:
                traverse(node.right)

        traverse(self.root)
        return output

    def postOrder(self):
        output = []
        def traverse(node):
            """inner recursion function to append the value to output list"""
            if not node:
                return

            if not node.left and not node.right:
                output.append(node.value)
                return
            else:
                traverse(node.left)

            if not node.right and not node.left:
                output.append(node.value)
                return
            else:
                traverse(node.right)

            output.append(node.value)

        traverse(self.root)
        return output

    def breadth_first(self):
        """method to do the breadth first search method"""
        output = []
        storage = Queue()

        storage.enqueue(self.root)

        while not storage.is_empty():
            front = storage.dequeue()
            output.append(front.value)

            if front.left:
                storage.enqueue(front.left)

            if front.right:
                storage.enqueue(front.right)

        return output

    def add(self,value):
        """method to add value to the tree using breadth first search method"""
        node = Node(value)
        storage = Queue()
        if not self.root:
            self.root = node
        else:
            storage.enqueue(self.root)
            while not storage.is_empty():
                front = storage.dequeue()

                if front.left:
                    storage.enqueue(front.left)
                else:
                    front.left = node
                    return

                if front.right:
                    storage.enqueue(front.right)
                else:
                    front.right = node
                    return



class BinarySearchTree(BinaryTree):

    def add(self,value):
        """function to add a value to the Binary Tree"""
        def traverse(node, add_node):
            """function to travel inside of the Tree and find the correct place to add the new value"""
            if add_node.value < node.value:# go to the left
                if not node.left:
                    node.left = add_node
                else:
                    traverse(node.left,add_node)

            else:# go to the right
                if not node.right:
                    node.right = add_node
                else:
                    traverse(node.right, add_node)

        new_node = Node(value)

        if not self.root:
            self.root=new_node
            return

        traverse(self.root, new_node)

    def contains(self,value):
        """function to check whether a given value is contains at least onece in the tree"""
        if value in self.preOrder():
            return True
        else:
            return False


if __name__ == "__main__":
    test = BinaryTree()
    test.add(100)
    test.add(50)
    test.add(200)
    test.add(25)
    test.add(75)
    test.add(155)
    print(test.breadth_first())
