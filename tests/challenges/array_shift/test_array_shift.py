from dsa import __version__
from dsa.challenges.array_shift.array_shift import *

def test_array_shift_1():
    expected = [2,4,5,6,8]
    actual = insertShiftArray([2,4,6,8], 5)
    assert expected == actual

def test_array_shift_2():
    expected = [4,8,15,16,23,42]
    actual = insertShiftArray([4,8,15,23,42], 16)
    assert expected == actual

def test_array_shift_3():
    expected = [2,4,6,8]
    actual = removeShiftArray([2,4,5,6,8])
    assert expected == actual

def test_array_shift_4():
    expected = [4,8,15,23,42]
    actual = removeShiftArray([4,8,15,16,23,42])
    assert expected == actual

