from dsa.challenges.queue_with_stacks.queue_with_stacks import *
import pytest

def test_enqueue_1():
    test = PseudoQueue()
    test.enqueue(5)
    tester = test.stack_one.__str__()
    assert tester == "[5]->NULL"


def test_enqueue_2():
    test = PseudoQueue()
    test.enqueue(20)
    test.enqueue(15)
    test.enqueue(10)
    test.enqueue(5)
    tester = test.stack_one.__str__()
    assert tester == "[5]->[10]->[15]->[20]->NULL"


def test_dequeue_1():
    test = PseudoQueue()
    test.enqueue(20)
    test.enqueue(15)
    test.enqueue(10)
    test.enqueue(5)
    test.dequeue()
    tester = test.stack_one.__str__()
    assert tester =="[5]->[10]->[15]->NULL"
    test.dequeue()
    tester_2 = test.stack_one.__str__()
    assert tester_2 == "[5]->[10]->NULL"

