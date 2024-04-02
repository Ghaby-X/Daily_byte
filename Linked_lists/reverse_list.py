# This question is asked by Facebook. Given a linked list, containing unique values, reverse it, and return the result.

# Ex: Given the following linked lists...

# 1->2->3->null, return a reference to the node that contains 3 which points to a list that looks like the following: 3->2->1->null
# 7->15->9->2->null, return a reference to the node that contains 2 which points to a list that looks like the following: 2->9->15->7->null
# 1->null, return a reference to the node that contains 1 which points to a list that looks like the following: 1->null

from Linked_List import create_linked_list, Node, print_node_chain


def reverse(lst):
    if (lst.head == None or lst.head.next == None):
        print_node_chain(lst.head)
        return
    
    p_reverse = None
    current = lst.head
    
    while current:
        temp = current.next
        current.next = p_reverse
        p_reverse = current
        current = temp
        
    
    print_node_chain(p_reverse)
    
    pass

#tests
reverse(create_linked_list([1,2,3])) # return 3 -> 2 -> 1 -> null
reverse(create_linked_list([7,15,9,2])) # return 2 -> 9 -> 15 -> 7 -> null
reverse(create_linked_list([1])) # return 1 -> null
