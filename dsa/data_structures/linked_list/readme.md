# Singly Linked Lists

[click here to see the code](linked_list.py)

[click here to see the tester code](../../../tests/data_structures/linked_list/test_%20linked_list.py)

## Challenge
<!-- Description of the challenge -->
- Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node.
- Within your LinkedList class, include a head property. Upon instantiation, an empty Linked List should be created.
    - Define a method called ```insert``` which takes any value as an argument and adds a new node with that value to the ```head``` of the list with an O(1) Time performance.
    - Define a method called ```includes``` which takes any value as an argument and returns a boolean result depending on whether that value exists as a Node’s value somewhere within the list.
    - Define a method called ```toString``` (or ```__str__``` in Python) which takes in no arguments and returns a string representing all the values in the Linked List, formatted as:
        - "{ a } -> { b } -> { c } -> NULL"

- Any exceptions or errors that come from your code should be semantic, capturable errors. For example, rather than a default error thrown by your language, your code should raise/throw a custom, semantic error that describes what went wrong in calling the methods you wrote for this lab.
- Be sure to follow your language/frameworks standard naming conventions (e.g. C# uses PascalCasing for all method and class names).

## Structure and Testing
Utilize the Single-responsibility principle: any methods you write should be clean, reusable, abstract component parts to the whole challenge. You will be given feedback and marked down if you attempt to define a large, complex algorithm in one function definition.

Write tests to prove the following functionality:

1. Can successfully instantiate an empty linked list
2. Can properly insert into the linked list
3. The head property will properly point to the first node in the linked list
4. Can properly insert multiple nodes into the linked list
5. Will return true when finding a value within the linked list that exists
6. Will return false when searching for a value in the linked list that does not exist
7. Can properly return a collection of all the values that exist in the linked list
## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
1. create the class to build nodes.
2. create the class to build linked lists, it has the following Attributes and Methods:
   1. head
   2. method insert
   3. method includes
   4. method `__str__`
3. Big O for insert method is the length of inserted values.
4. Big O for includes method is the length of linked List.
5. Big O for the to string method is the length of the linked list.


## API
<!-- Description of each method publicly available to your Linked List -->
1. insert method will take a list of values, insert them before the head of the linked list. Use a for loop to check the length of value to be inserted, link them together, then reset the linked list head to the new head value, link the last inserted value's next value to the previous head of the list.
2. includes method use while loop to check every single value of the linked list, if it find a match, then return True, otherwise, Faluse.
3. the to string method use the while loop too, find every value in the linked list, convert to string, format to { value } and added "->" between values and then output the whole values as one signle string.
