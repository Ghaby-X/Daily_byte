# This question is asked by Google. Given a linked list and a value, remove all nodes containing the provided value, and return the resulting list.

# Ex: Given the following linked lists and values...

# 1->2->3->null, value = 3, return 1->2->null
# 8->1->1->4->12->null, value = 1, return 8->4->12->null
# 7->12->2->9->null, value = 7, return 12->2->9->null

from Linked_List import create_linked_list, Node, print_node_chain

def remove_all_nodes(lst, val):
    fast_pointer = lst.head
    answer = Node(4) #initial dum_dum
    slow_pointer = answer
    
    while(fast_pointer):
        if fast_pointer.val != val:
            slow_pointer.next = fast_pointer
            slow_pointer = slow_pointer.next

        fast_pointer = fast_pointer.next
        
        
    
    print_node_chain(answer.next)
    return

remove_all_nodes(create_linked_list([1,2,3]), 3) # return 1->2->null
remove_all_nodes(create_linked_list([8,1,1,4,12]), 1) # return 8->4->12->null
remove_all_nodes(create_linked_list([7,12,2,9]), 7) # return 12->2->9->null