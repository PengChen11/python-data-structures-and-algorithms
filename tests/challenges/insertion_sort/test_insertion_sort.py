from dsa.challenges.insertion_sort.insertion_sort import insertion_sort

def test_insertion_sort1():
    arr = [8,4,23,42,16,15]
    actural = insertion_sort(arr)
    expected = [4, 8, 15, 16, 23, 42]
    assert actural == expected


def test_insertion_sort2():

    arr = [5,12,7,5,5,7]
    actural = insertion_sort(arr)
    expected = [5, 5, 5, 7, 7, 12]
    assert actural == expected


def test_insertion_sort3():

    arr = [20,18,12,8,5,-2]
    actural = insertion_sort(arr)
    expected = [-2,5,8,12,18,20]
    assert actural == expected


def test_insertion_sort5():

    arr = [2,3,5,7,13,11]
    actural = insertion_sort(arr)
    expected = [2,3,5,7,11,13]
    assert actural == expected
