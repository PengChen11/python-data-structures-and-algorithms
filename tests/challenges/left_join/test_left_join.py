from dsa.data_structures.hash_table.hash_table import HashTable
from dsa.challenges.left_join.left_join import left_join

def table_build_1():
    hash_table = HashTable(10)
    hash_table.add('fond', 'enamored')
    hash_table.add('wrath', 'anger')
    hash_table.add('diligent', 'employed')
    hash_table.add('outift', 'garb')
    hash_table.add('guide', 'usher')
    return hash_table

def table_build_2():
    hash_table = HashTable(10)
    hash_table.add('fond', 'averse')
    hash_table.add('wrath', 'delight')
    hash_table.add('diligent', 'idle')
    hash_table.add('guide', 'follow')
    hash_table.add('flow', 'jam')
    return hash_table

def test_left_join():
    table_1 = table_build_1()
    table_2 = table_build_2()
    actural = left_join(table_1,table_2)
    expected = [
        ['wrath', 'anger', 'delight'],
        ['fond', 'enamored', 'averse'],
        ['diligent', 'employed', 'idle'],
        ['guide', 'usher', 'follow'],
        ['outift', 'garb', None]
    ]
    assert actural == expected
