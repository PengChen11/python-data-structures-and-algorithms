from dsa import __version__
from dsa.challenges.array_binary_search.array_binary_search import BinarySearch

def test_1():
    expected = 2
    actual = BinarySearch([4,8,15,16,23,42], 15)
    assert expected == actual

def test_2():
    expected = -1
    actual = BinarySearch([11,22,33,44,55,66,77], 90)
    assert expected == actual

def test_3():
    expected = 63
    actual = BinarySearch(list(range(100)), 63)
    assert expected == actual

def test_4():
    expected = 6311
    actual = BinarySearch(list(range(10000)), 6311)
    assert expected == actual

def test_5():
    expected = 54321
    actual = BinarySearch(list(range(100000)), 54321)
    assert expected == actual
