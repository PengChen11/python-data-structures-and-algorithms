from dsa.data_structures.hash_table.hash_table import HashTable

def left_join(table_1, table_2):
    """function to left join two hash tables"""
    output = []
    for elem in table_1.table:
        if elem:
            current = elem.head_val
            while current:
                value_1 = current.value
                value_2 = table_2.get(value_1[0])
                value_1.append(value_2)
                output.append(value_1)
                current = current.next_val

    return output
