from dsa.data_structures.linked_list.linked_list import *

import pytest


def test_instantiate():
    tester = Linked_List()
    assert tester.head_val==None


def test_insert_single(init_values):
    test_list = Linked_List()
    test_list.insert(['Day1: Mon'])
    tester=test_list.__str__()
    assert tester == '{ Day1: Mon } -> NULL'


def test_insert_array():
    test_list = Linked_List()
    test_list.insert([[1,2,3],[4,5,6]])
    tester=test_list.__str__()
    assert tester == '{ [1, 2, 3] } -> { [4, 5, 6] } -> NULL'


def test_head(init_values):
    test_list = Linked_List()
    test_list.insert(init_values)
    tester = test_list.head_val.val
    assert tester == 'Day2: Tue'


def test_insert_multiple(init_values, muti_values):
    test_list = Linked_List()
    test_list.insert(init_values)
    test_list.insert(muti_values)
    tester=test_list.__str__()
    assert tester == '{ Day7: Sun } -> { Day1: Mon } -> { Day2: Tue } -> { Day3: Wed } -> { Day4: Thu } -> { Day5: Fri } -> NULL'


def test_search_value_true(init_values):
    test_list = Linked_List()
    test_list.insert(init_values)
    test_1 = test_list.includes('Day2: Tue')
    test_2 = test_list.includes('Day5: Fri')
    assert test_1 == True
    assert test_2 == True


def test_search_array():
    test_list = Linked_List()
    test_list.insert([[1,2,3],[4,5,6]])
    tester=test_list.includes([4,5,6])
    assert tester == True


def test_search_value_false(init_values):
    test_list = Linked_List()
    test_list.insert(init_values)
    test_1 = test_list.includes('Day1: Mon')
    test_2 = test_list.includes('Day5: Tue')
    assert test_1 == False
    assert test_2 == False


def test_return_all(init_values):
    test_list = Linked_List()
    test_list.insert(init_values)
    tester = test_list.__str__()
    assert tester == '{ Day2: Tue } -> { Day3: Wed } -> { Day4: Thu } -> { Day5: Fri } -> NULL'




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

