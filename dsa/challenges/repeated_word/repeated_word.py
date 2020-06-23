import re
from dsa.data_structures.hash_table.hash_table import HashTable

def repeated_word(input_str, counter=False, key=None, freq=False):
    """find the 1st repeated word in a long string. If counter arg is True, then return a string showing the words counter"""
    #use regex to replace all non alphabetic characters with a space
    pure_text = re.sub('[^a-zA-Z]+', ' ', input_str)
    word_list = [word.lower() for word in pure_text.split()]

    table_length = len(input_str)
    collection = HashTable(table_length)

    frequent_word = None
    frenquency = 0

    output = ''

    for word in word_list:
        word_check = collection.contains(word)
        if not word_check:
            collection.add(word,1)
        else:
            if counter == False and key == None and freq == False:
                return word

            else:
                new_val = collection.get(word)+1

                collection.add(word, new_val)
                if freq == True:
                    frenquency = new_val
                    frequent_word = word

    if counter == True:
        output += "Here's the words counter: \n"
        for elem in collection.table:
            if elem:
                if not elem.head_val.next_val:
                    output+=str(elem.head_val.val)+'\n'
                else:
                    current = elem.head_val
                    while current is not None:
                        output += str(current.val) + '\n'
                        current = current.next_val
    if key:
        times = collection.get(key)
        output += f'The word "{key}" appears {times} time(s).' + '\n'

    if freq == True:
        output += f'"{frequent_word}" is the most frequently used word, it repeated {frenquency} times' + '\n'

    return output

if __name__ == "__main__":
    test = "Once upon a time, there was a brave princess who..."
    actural = repeated_word(test)
    expected = 'a'
    assert actural==expected

    test2 = repeated_word(test, key='once', freq=True)

    print(test2)

