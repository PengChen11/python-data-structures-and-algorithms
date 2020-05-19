from textwrap import dedent

class Node:
    def __init__(self, val=None):
        self.val = val
        self.next_val = None

class Linked_List:
    def __init__(self):
        self.head_val = None

    def insert(self,val_list):
        # my own assert to handle errors
        assert (type(val_list)==list), "The value(s) to be inserted needs be a list"
        assert (val_list != []), "the value(s) to be inserted can't be empty list"
        if len(val_list) ==1 and val_list != []:
            new_node = Node(val_list[0])
            new_node.next_val = self.head_val
            self.head_val = new_node
        else:#handle mutiply insertioin
            new_node_head = Node(val_list[0])
            new_node_after = Node(val_list[1])
            new_node_head.next_val = new_node_after

            for i in range(2,len(val_list)):
                new_node_next = Node(val_list[i])
                new_node_after.next_val = new_node_next
                new_node_after = new_node_next

            new_node_after.next_val=self.head_val
            self.head_val = new_node_head

    def includes(self,search_value):
        current=self.head_val
        while current is not None:
            if current.val == search_value:
                return True
            current = current.next_val
        return False


    def append(self,value):
        new_node = Node(value)
        current = self.head_val
        if current is None:
            self.head_val = new_node
        else:
            a=0
            while current is not None:
                if current.next_val is None:
                    current.next_val = new_node
                    break
                current = current.next_val


    def insertBefore(self,value,new_val):
        new_node = Node(new_val)
        current = self.head_val
        find = False
        while current is not None:
            if current.val == value:
                self.insert([new_val])
                find = True
                break
            elif current.next_val is not None and current.next_val.val == value:
                new_node.next_val = current.next_val
                current.next_val =new_node
                find = True
                break
            current = current.next_val
        if find is False:
            raise Exception("Can't find the value")


    def insertAfter(self,value,new_val):
        new_node = Node(new_val)
        current = self.head_val
        find = False
        while current is not None:
            if current.val == value:
                new_node.next_val=current.next_val
                current.next_val=new_node
                find = True
                break
            current = current.next_val
        if find is False:
            raise Exception("Can't find the value")


    # def remove(self,value):
    #     current = self.head_val
    #     if current == value:
    #         self.head_val = current.next_val
    #     else:
    #         while current is not None:
    #             if current.val == value:
    #                 current
    #             current = current.next_val


    def __str__(self):
        current=self.head_val
        val_list = []
        # convert all the linked list values into required format and append to an list for output.
        while current is not None:
            val_list.append('{ '+ str(current.val) +' } -> ')
            current=current.next_val
        #in the end of the output list, add NULL.
        val_list.append('NULL')

        output = ''
        return output.join(val_list)



# if __name__ == "__main__":
#     test_list = Linked_List()
#     test_list.insert([1,2,3,4])
#     test_list.insertAfter(4,5)
#     print(test_list.__str__())


