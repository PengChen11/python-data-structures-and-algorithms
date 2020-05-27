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


    def __str__(self):
        output = ""
        current = self.top

        while current:
            output += f"{ [current.val]}->"
            current = current.next
        return output + "NULL"



class PseudoQueue:
    def __init__(self):
        self.stack_one = Stack()
        self.stack_two = Stack()


    def enqueue(self, value):
        self.stack_one.push(value)
        if self.stack_one.top.next == None:
            self.front = self.stack_one.top


    def dequeue(self):
        while self.stack_one.top:
            node = self.stack_one.pop()
            self.stack_two.push(node)
        queue_front = self.stack_two.pop()
        self.front = self.stack_two.top
        while self.stack_two.top:
            node = self.stack_two.pop()
            self.stack_one.push(node)
        return queue_front




