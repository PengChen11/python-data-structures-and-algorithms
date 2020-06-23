from dsa.data_structures.linked_list.linked_list import *

import pytest


def test_instantiate():
    tester = Linked_List()
    assert(tester.head_val==None), 'Error occured when instantiate a linked list'


def test_insert_single(init_values):
    test_list = Linked_List()
    test_list.insert(['Day1: Mon'])
    tester=test_list.__str__()
    assert (tester == '{ Day1: Mon } -> NULL'), 'Failed to insert a single value to linked list'


def test_insert_array():
    test_list = Linked_List()
    test_list.insert([[1,2,3],[4,5,6]])
    tester=test_list.__str__()
    assert (tester == '{ [1, 2, 3] } -> { [4, 5, 6] } -> NULL'), 'Failed to insert a list into the linked list'


def test_head(init_values):
    test_list = Linked_List()
    test_list.insert(init_values)
    tester = test_list.head_val.value
    assert (tester == 'Day2: Tue'),'HEAD test failed'


def test_insert_multiple(init_values, muti_values):
    test_list = Linked_List()
    test_list.insert(init_values)
    test_list.insert(muti_values)
    tester=test_list.__str__()
    assert (tester == '{ Day7: Sun } -> { Day1: Mon } -> { Day2: Tue } -> { Day3: Wed } -> { Day4: Thu } -> { Day5: Fri } -> NULL'), 'Failed to insert multiple values into linked list'


def test_search_value_true(init_values):
    test_list = Linked_List()
    test_list.insert(init_values)
    test_1 = test_list.includes('Day2: Tue')
    test_2 = test_list.includes('Day5: Fri')
    assert (test_1 == True and test_2 == True), 'Failed to search inside the linked list'


def test_search_array():
    test_list = Linked_List()
    test_list.insert([[1,2,3],[4,5,6]])
    tester=test_list.includes([4,5,6])
    assert (tester == True),'Failed to search an array inside the linked list'


def test_search_value_false(init_values):
    test_list = Linked_List()
    test_list.insert(init_values)
    test_1 = test_list.includes('Day1: Mon')
    test_2 = test_list.includes('Day5: Tue')
    assert (test_1 == False and test_2 == False),'Failed to search something not in the linked list'


def test_return_all(init_values):
    test_list = Linked_List()
    test_list.insert(init_values)
    tester = test_list.__str__()
    assert (tester == '{ Day2: Tue } -> { Day3: Wed } -> { Day4: Thu } -> { Day5: Fri } -> NULL'),'Failed to return all values inside of the linked list'


def test_append(insertion_val):
    test_list = Linked_List()
    test_list.insert(insertion_val)
    test_list.append(5)
    tester = test_list.__str__()
    assert tester == '{ 1 } -> { 3 } -> { 2 } -> { 5 } -> NULL'


def test_append_1():
    test_list = Linked_List()
    test_list.append(1)
    tester = test_list.head_val.value
    assert (tester == 1),'Error when appending value to an empty linked list.'


def test_insertBefore_1(insertion_val):
    test_list = Linked_List()
    test_list.insert(insertion_val)
    test_list.insertBefore(3,5)
    tester = test_list.__str__()
    assert (tester == '{ 1 } -> { 5 } -> { 3 } -> { 2 } -> NULL'), 'Insert before error.'


def test_insertBefore_2(insertion_val):
    test_list = Linked_List()
    test_list.insert(insertion_val)
    test_list.insertBefore(1,5)
    tester = test_list.__str__()
    assert (tester == '{ 5 } -> { 1 } -> { 3 } -> { 2 } -> NULL'), 'Insert before error.'



def test_insertBefore_3(insertion_val_2):
    test_list = Linked_List()
    test_list.insert(insertion_val_2)
    test_list.insertBefore(2,5)
    tester = test_list.__str__()
    assert (tester == '{ 1 } -> { 5 } -> { 2 } -> { 2 } -> NULL'), 'Insert before error.'


def test_insertBefore_4(insertion_val):
    test_list = Linked_List()
    test_list.insert(insertion_val)
    with pytest.raises(Exception):
        assert test_list.insertBefore(4,5)



def test_insertAfter_1(insertion_val):
    test_list = Linked_List()
    test_list.insert(insertion_val)
    test_list.insertAfter(3,5)
    tester = test_list.__str__()
    assert (tester == '{ 1 } -> { 3 } -> { 5 } -> { 2 } -> NULL'), 'insertAfter error.'


def test_insertAfter_2(insertion_val):
    test_list = Linked_List()
    test_list.insert(insertion_val)
    test_list.insertAfter(2,5)
    tester = test_list.__str__()
    assert (tester == '{ 1 } -> { 3 } -> { 2 } -> { 5 } -> NULL'), 'insertAfter error.'


def test_insertAfter_3(insertion_val_2):
    test_list = Linked_List()
    test_list.insert(insertion_val_2)
    test_list.insertAfter(2,5)
    tester = test_list.__str__()
    assert (tester == '{ 1 } -> { 2 } -> { 5 } -> { 2 } -> NULL'), 'insertAfter error.'


def test_insertAfter_4(insertion_val):
    test_list = Linked_List()
    test_list.insert(insertion_val)
    with pytest.raises(Exception):
        assert test_list.insertBefore(4,5)


def test_remove_1(insertion_val):
    test_list = Linked_List()
    test_list.insert(insertion_val)
    test_list.remove(1)
    tester = test_list.__str__()
    assert (tester == '{ 3 } -> { 2 } -> NULL'), '.remove() is not working'


def test_remove_2(insertion_val):
    test_list = Linked_List()
    test_list.insert(insertion_val)
    test_list.remove(2)
    tester = test_list.__str__()
    assert (tester == '{ 1 } -> { 3 } -> NULL'), '.remove() is not working'


def test_reverseSearch(reverse_val):
    test_list = Linked_List()
    test_list.insert(reverse_val)
    tester1 = test_list.reverseSearch(0)
    tester2 = test_list.reverseSearch(2)
    assert (tester1 == 2),'reversed search method is not working'
    assert (tester2 == 3),'reversed search method is not working'
    with pytest.raises(Exception):
        assert test_list.reverseSearch(6)
    with pytest.raises(Exception):
        assert test_list.reverseSearch(-1)




@pytest.fixture
def init_values():
    return [
        'Day2: Tue',
        'Day3: Wed',
        'Day4: Thu',
        'Day5: Fri'
        ]

@pytest.fixture
def muti_values():
    return [
        'Day7: Sun',
        'Day1: Mon'
    ]

@pytest.fixture
def insertion_val():
    return [
        1,
        3,
        2
    ]

@pytest.fixture
def insertion_val_2():
    return [
        1,
        2,
        2
    ]

@pytest.fixture
def reverse_val():
    return [
        1,
        3,
        8,
        2
    ]
