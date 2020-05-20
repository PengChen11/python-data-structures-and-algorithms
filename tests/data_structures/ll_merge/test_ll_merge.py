from dsa.data_structures.ll_merge.ll_merge import mergeLists
from dsa.data_structures.linked_list.linked_list import *

import pytest

def test_merge_1(list1, list2):
    link_list_1 = Linked_List()
    link_list_1.insert(list1[0])
    link_list_2 = Linked_List()
    link_list_2.insert(list2[0])
    merge = mergeLists(link_list_1,link_list_2)
    assert merge.__str__()=='{ 1 } -> { 5 } -> { 3 } -> { 9 } -> { 2 } -> { 4 } -> NULL'


def test_merge_2(list1, list2):
    link_list_1 = Linked_List()
    link_list_1.insert(list1[1])
    link_list_2 = Linked_List()
    link_list_2.insert(list2[0])
    merge = mergeLists(link_list_1,link_list_2)
    assert merge.__str__()=='{ 1 } -> { 5 } -> { 3 } -> { 9 } -> { 4 } -> NULL'

def test_merge_3(list1, list2):
    link_list_1 = Linked_List()
    link_list_1.insert(list1[0])
    link_list_2 = Linked_List()
    link_list_2.insert(list2[1])
    merge = mergeLists(link_list_1,link_list_2)
    assert merge.__str__()=='{ 1 } -> { 5 } -> { 3 } -> { 9 } -> { 2 } -> NULL'



@pytest.fixture
def list1():
    return [
        [1,3,2],
        [1,3]
    ]

@pytest.fixture
def list2():
    return [
        [5,9,4],
        [5,9]
    ]
