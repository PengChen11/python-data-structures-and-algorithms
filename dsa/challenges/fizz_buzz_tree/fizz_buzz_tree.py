import sys
sys.path.append("/Users/pengchen/Library/Mobile Documents/com~apple~CloudDocs/SCHOOL/Code_Fellows/401/python/python-data-structures-and-algorithms")

from dsa.data_structures.tree.tree import *

def fizz_buzz_tree(tree):
    storage = tree.breadth_first()
    output = BinaryTree()
    for i in storage:
        if i % 15 == 0:
            output.add("FizzBuzz")
        elif i % 3 ==0 :
            output.add("Fizz")
        elif i % 5 ==0 :
            output.add("Buzz")
        else:
            output.add(str(i))
    return output


if __name__ == "__main__":
    test = BinaryTree()
    test.add(100)
    test.add(11)
    test.add(21)
    test.add(4)
    test.add(15)
    test.add(75)
    test.add(112)

    print(fizz_buzz_tree(test).breadth_first())
