# this part is left here casue I need to ask JB a question next Week.
# import sys
# sys.path.append("~/Library/Mobile\ Documents/com~apple~CloudDocs/SCHOOL/Code_Fellows/401/python/python-data-structures-and-algorithms/dsa/data_structures/linked_list/")

# from linked_list import *



class Node:
    """create new node"""
    def __init__(self, val=None):
        self.val = val
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
        return pop_node.val


    def peek(self):
        try:
            return self.top.val
        except:
            print('The Stack is empty now')

    def isEmpty(self):
        return self.top == None


class Queue:
    def __init__(self,front=None):
        self.front = front
        self.rear = self.front


    def enqueue(self,value):
        new_node = Node(value)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node


    def dequeue(self):
        try:
            dequeue_node = self.front
            self.front = self.front.next
            dequeue_node.next = None
        except:
            print('The Queue is empty now')
        return dequeue_node.val


    def peek(self):
        try:
            return self.front.val
        except:
            print('The Queue is empty now')


    def inEmpty(self):
        return self.front == None

