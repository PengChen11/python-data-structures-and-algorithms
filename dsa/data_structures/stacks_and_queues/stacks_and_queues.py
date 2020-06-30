# this part is left here casue I need to ask JB a question next Week.
# import sys
# sys.path.append("~/Library/Mobile\ Documents/com~apple~CloudDocs/SCHOOL/Code_Fellows/401/python/python-data-structures-and-algorithms/dsa/data_structures/linked_list/")

# from dsa.data_structures.linked_list.linked_list import *



class Node:
    """create new node"""
    def __init__(self, value=None):
        self.value = value
        self.next = None


class Stack:
    def __init__(self,top=None):
        self.top = top


    def push(self,value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node


    def pop(self):
        try:
            pop_node = self.top
            self.top = self.top.next
            pop_node.next = None
        except:
            print('The Stack is empty now')
        return pop_node.value


    def peek(self):
        try:
            return self.top.value
        except:
            print('The Stack is empty now')

    def isEmpty(self):
        return self.top == None


class Queue:
    def __init__(self,front=None):
        self._front = front
        self._rear = self._front


    def enqueue(self,value):
        new_node = Node(value)
        if self._front is None:
            self._front = self._rear = new_node
        else:
            self._rear.next = new_node
            self._rear = new_node


    def dequeue(self):
        try:
            dequeue_node = self._front
            self._front = self._front.next
            # dequeue_node.next = None
        except:
            return None
        return dequeue_node.value


    def peek(self):
        try:
            return self._front.value
        except:
            return None


    def isEmpty(self):
        return self._front == None

if __name__ == "__main__":
    pass
