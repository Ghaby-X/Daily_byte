# This question is asked by Facebook. Given a linked list and a value n, remove the nth to last node and return the resulting list.

# Ex: Given the following linked lists...

# 1->2->3->null, n = 1, return 1->2->null
# 1->2->3->null, n = 2, return 1->3->null
# 1->2->3->null, n = 3, return 2->3->null

from Linked_List import Node, create_linked_list,print_node_chain

def remove_Nth_from_last(lst, idx):
    lst_size = lst.size
    rm_id = lst_size - idx + 1
    
    
    if rm_id == 1:
        answer = lst.head.next
        print_node_chain(answer)
        return
    
    answer = lst.head
    
    pointer = answer
    
    count = 1
    while(True):
        jump_signal = count == (rm_id - 1)
        
        if(jump_signal):
            pointer.next = pointer.next.next
            break
        
        pointer = pointer.next
        count = count + 1

        
    print_node_chain(answer)
    return

remove_Nth_from_last(create_linked_list([1,2,3]), 1) # return 1->2->null
remove_Nth_from_last(create_linked_list([1,2,3]), 2) # return 1->3->null
remove_Nth_from_last(create_linked_list([1,2,3]), 3) # return 2->3->null