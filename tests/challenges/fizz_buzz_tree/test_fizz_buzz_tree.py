from dsa.challenges.fizz_buzz_tree.fizz_buzz_tree import *

def test_fizz_buzz_1():
    test = BinaryTree()
    test.add(75)
    test.add(5)
    test.add(3)
    assert fizz_buzz_tree(test).preOrder() == ['FizzBuzz', 'Buzz', 'Fizz']

def test_fizz_buzz_2():
    test = BinaryTree()
    test.add(75)
    test.add(5)
    test.add(3)
    test.add(4)
    test.add(112)

    assert fizz_buzz_tree(test).preOrder() == ['FizzBuzz', 'Buzz', '4','112' ,'Fizz']

def test_fizz_buzz_3():
    test = BinaryTree()
    test.add(100)
    test.add(11)
    test.add(21)
    test.add(4)
    test.add(15)
    test.add(75)
    test.add(112)
    assert fizz_buzz_tree(test).preOrder() == ['Buzz', '11', '4', 'FizzBuzz', 'Fizz', 'FizzBuzz', '112']


