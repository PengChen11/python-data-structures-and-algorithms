from dsa.data_structures.linked_list.linked_list import *

def mergeLists(LL_1,LL_2):
    """function to take two linked list, return a zipped linked"""

    LL_1_current = LL_1.head_val
    LL_2_current = LL_2.head_val
    middle_man_1 = LL_1_current.next_val
    middle_man_2 = LL_2_current.next_val

    while LL_1_current is not None and LL_2_current is not None:

        if middle_man_1 is None and middle_man_2 is not None:
            LL_1_current.next_val = LL_2_current
            LL_2_current.next_val = middle_man_2
        else:
            LL_1_current.next_val = LL_2_current
            LL_2_current.next_val = middle_man_1

        LL_1_current = middle_man_1
        LL_2_current = middle_man_2

        if middle_man_1 is not None and middle_man_2 is not None:
            middle_man_1 = middle_man_1.next_val
            middle_man_2 = middle_man_2.next_val

    return LL_1


if __name__ == "__main__":
    list1=[
        [1,3,2],
        [1,3]
    ]

    list2=[
        [5,9,4],
        [5,9]
    ]

    link_list_1 = Linked_List()
    link_list_1.insert(list1[0])

    link_list_2 = Linked_List()
    link_list_2.insert(list2[1])

    merge = mergeLists(link_list_1,link_list_2)
    print(merge.__str__())
