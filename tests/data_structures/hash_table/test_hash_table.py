from dsa.data_structures.hash_table.hash_table import *
import random
import string

def build_hash_table(size):
    test = HashTable(size)
    test.add('Name','Peter')
    test.add('Sex','male')
    test.add('Age',25)
    return test


def test_add_to_hash_table():
    test = build_hash_table(5)
    assert test.contains('Name')
    assert test.contains('Sex')
    assert test.contains('Age')


def test_get_hash_table():
    test = build_hash_table(5)
    assert test.get('Name') == 'Peter'


def test_get_none_hash_table():
    test = build_hash_table(5)
    assert test.get('Name') == 'Peter'
    assert test.get('sex') == None # lower case letter mis-match
    assert test.get('age') == None


def test_handel_collision():
    test = build_hash_table(5)
    assert str(test.table[1]) == "{ ['Sex', 'male'] } -> { ['Age', 25] } -> NULL"


def test_get_from_collision():
    test = build_hash_table(5)
    assert test.get('Sex') == 'male'
    assert test.get('Age') == 25


def test_hash_key_range():
    char = string.ascii_letters
    test = HashTable(5)
    for i in range(1000):
        key = ''.join(random.choice(char) for i in range(10))
        assert test.hash(key) <= 4
        assert test.hash(key) >= 0

