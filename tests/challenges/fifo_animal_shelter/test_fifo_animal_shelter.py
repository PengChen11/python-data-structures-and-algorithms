from dsa.challenges.fifo_animal_shelter.fifo_animal_shelter import *
import pytest

def test_enqueue():
    test = AnimalShelter()
    test.enqueue("cat","Kitty")
    test.enqueue("dog","Bobby")
    test.enqueue("cat","Isaa")
    test.enqueue("dog","T-bag")
    tester = str(test)
    assert tester == "cat Kitty & dog Bobby & cat Isaa & dog T-bag & are in the shelter now"


def test_enqueue_error():
    test = AnimalShelter()
    with pytest.raises(Exception):
        assert test.enqueue("pig", "Peppa")


def test_dequeue_cat():
    dequeue_animal = []
    test = AnimalShelter()
    test.enqueue("cat","Kitty")
    test.enqueue("dog","Bobby")
    test.enqueue("cat","Isaa")
    test.enqueue("dog","T-bag")
    a=test.dequeue("cat")
    dequeue_animal.append(str(a))
    b=test.dequeue("cat")
    dequeue_animal.append(str(b))
    assert dequeue_animal == ['I am a cat, my name is Kitty', 'I am a cat, my name is Isaa']


