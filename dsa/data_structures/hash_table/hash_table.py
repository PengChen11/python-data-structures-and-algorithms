from dsa.data_structures.linked_list.linked_list import *

class HashTable:
    def __init__(self,size):
        self.size = size
        self.table = [None]*self.size

    def _value(self, LL, key, value=None):
        """
        when giving the value, this method adds the key and value to the hash table; if key already exsists, then just update the value;
        when value is NOT givin, this method return the value matching the key, or None
        """
        if value:
            current = LL.head_val
            while current is not None:
                if current.val[0] == key:
                    current.val[1] = value
                    return
                current = current.next_val
            LL.append([key, value])

        else:
            current = LL.head_val
            while current is not None:
                if current.val[0] == key:
                    return current.val[1]
                current = current.next_val
            return None

    def add(self, key, value):
        '''
        this method hashs the key, and add the key and value pair to the table;
        if key already exsist, update the value;
        if multipul keys using the same hashed_key,  handle collisions
        '''
        hashed_key = self.hash(key)

        if not self.table[hashed_key]:
            self.table[hashed_key] = Linked_List()

        self._value(self.table[hashed_key], key, value)



    def get(self, key):
        '''This method gets the value for the key.'''
        hashed_key = self.hash(key)
        if self.table[hashed_key]:
            return self._value(self.table[hashed_key], key)
        return None

    def contains(self,key):
        '''this method checks whether a key is contained in the hash table'''
        hashed_key = self.hash(key)
        key_check = self._value(self.table[hashed_key],  key)
        if self.table[hashed_key] and key_check:
            return True
        return False

    def hash(self, key):
        '''this method hashes the key'''
        total = 0
        for char in key:
            total += ord(char)

        total *= 1234
        hash_key = total % self.size
        return hash_key



if __name__ == "__main__":
    test = HashTable(5)
    test.add('Name','Peter')
    test.add('Sex','male')
    test.add('Age',25)
    for thing in range(len(test.table)):
        if test.table[thing]:
            print(f'the {thing} index value is {str(test.table[thing])}')
    print(test.get('Name'))
    print(test.contains('Name'))

