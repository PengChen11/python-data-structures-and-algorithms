from dsa.challenges.merge_sort.merge_sort import merge_sort

def test_merge_sort1():
    arr = [8,4,23,42,16,15]
    merge_sort(arr)
    actural = arr
    expected = [4, 8, 15, 16, 23, 42]
    assert actural == expected

def test_merge_sort2():
    arr = [5,12,7,5,5,7]
    merge_sort(arr)
    actural = arr
    expected = [5, 5, 5, 7, 7, 12]
    assert actural == expected


def test_merge_sort3():
    arr = [20,18,12,8,5,-2]
    merge_sort(arr)
    actural = arr
    expected = [-2,5,8,12,18,20]
    assert actural == expected

def test_merge_sort4():
    arr = [2,3,5,7,13,11]
    merge_sort(arr)
    actural = arr
    expected = [2,3,5,7,11,13]
    assert actural == expected

def test_merge_sort5():
    arr = [9,8,7,6,5,4,3,2,1]
    merge_sort(arr)
    actural = arr
    expected = [1,2,3,4,5,6,7,8,9]
    assert actural == expected
