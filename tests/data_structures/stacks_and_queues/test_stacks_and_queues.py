from dsa.data_structures.stacks_and_queues.stacks_and_queues import *
import pytest


def test_stack_push_one():
    test_stack = Stack()
    test_stack.push('tester_1')
    tester = test_stack.top.val
    assert (tester == 'tester_1'),"push to stack failed"


def test_stack_push_multiple():
    test_stack = Stack()
    test_stack.push('tester_1')
    test_stack.push('tester_2')
    test_stack.push('tester_3')
    tester = test_stack.top.val
    assert (tester == 'tester_3'),"push multiple values to stack failed"


def test_stack_pop():
    test_stack = Stack()
    test_stack.push('tester_1')
    test_stack.push('tester_2')
    test_stack.push('tester_3')
    tester = test_stack.pop()
    assert (tester == 'tester_3'),"pop top value from stack failed"


def test_stack_pop_multiple():
    test_stack = Stack()
    test_stack.push('tester_1')
    test_stack.push('tester_2')
    test_stack.pop()
    test_stack.pop()
    tester = test_stack.top
    assert (tester is None),"pop top value from stack failed"


def test_stack_peep():
    test_stack = Stack()
    test_stack.push('tester_1')
    tester = test_stack.peek()
    assert (tester == 'tester_1'),"Something goes wrong when peeking from the stack"


def test_stack_init():
    test_stack = Stack()
    tester = test_stack.top
    assert (tester is None), "Something goes wrong when init the stack"


def test_stack_exception():
    test_stack = Stack()
    with pytest.raises(Exception):
        assert test_stack.pop()
    with pytest.raises(Exception):
        assert test_stack.peek()



def test_queue_enqueue_one():
    test_queue = Queue()
    test_queue.enqueue('tester_1')
    tester = test_queue.front.val
    assert (tester == 'tester_1'),'Something goes wrong when enqueuing'


def test_queue_enqueue_multiple():
    test_queue = Queue()
    test_queue.enqueue('tester_1')
    test_queue.enqueue('tester_2')
    test_queue.enqueue('tester_3')
    tester = test_queue.front.next.next.val
    assert (tester == 'tester_3'),'Something goes wrong when enqueuing multiple values'


def test_queue_dequeue():
    test_queue = Queue()
    test_queue.enqueue('tester_1')
    test_queue.enqueue('tester_2')
    test_queue.enqueue('tester_3')
    tester = test_queue.dequeue()
    assert (tester == 'tester_1'),'Something goes wrong when dequeuing'


def test_queue_peek():
    test_queue = Queue()
    test_queue.enqueue('tester_1')
    test_queue.enqueue('tester_2')
    test_queue.enqueue('tester_3')
    tester = test_queue.peek()
    assert (tester == 'tester_1'),'Something goes wrong when peeking the queue'


def test_queue_dequeue_multiple():
    test_queue = Queue()
    test_queue.enqueue('tester_1')
    test_queue.enqueue('tester_2')
    test_queue.enqueue('tester_3')
    test_queue.dequeue()
    test_queue.dequeue()
    test_queue.dequeue()
    tester = test_queue.front
    assert (tester is None),'Something goes wrong when dequeuing every value'


def test_queue_init():
    test_queue = Queue()
    tester = test_queue.front
    assert(tester is None), "something goes wrong when init queue"


def test_queue_exception():
    test_queue = Queue()
    with pytest.raises(Exception):
        assert test_queue.dequeue()
    with pytest.raises(Exception):
        assert test_queue.peek()
