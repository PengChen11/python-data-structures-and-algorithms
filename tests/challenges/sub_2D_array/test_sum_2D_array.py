from dsa.challenges.sum_2D_array.sum_2D_array import *

def test_1():
    expected = [6, 15, 18]
    actural = sum_2D_array([ [1, 2, 3], [3, 5, 7], [1, 7, 10] ])
    assert actural == expected

def test_2():
    expected = [6, 5, 20]
    actural = sum_2D_array([ [0, 1, 5], [-4, 7, 2], [-3, 12, 11] ])
    assert actural == expected
