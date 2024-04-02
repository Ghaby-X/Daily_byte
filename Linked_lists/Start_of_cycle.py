# This question is asked by Apple. Given a potentially cyclical linked list where each value is unique, return the node at which the cycle starts. If the list does not contain a cycle, return null.

# Ex: Given the following linked lists...

# 1->2->3, return null
# 1->2->3->4->5->2 (5 points back to 2), return a reference to the node containing 2
# 1->9->3->7->7 (7 points to itself), return a reference to the node containing 7

from Linked_List import create_linked_list, Node

def start_of_cycle(lst):
    cycle_start_reference = None
    current = lst.head
    
    dictionary = set()
    
    while (current):
        
        if current.val in dictionary:
            cycle_start_reference = current
            print(cycle_start_reference.val)
            return
        
        dictionary.add(current.val)
        current = current.next
    
    print('None')
    return

start_of_cycle(create_linked_list([1,2,3])) # -->> return null
start_of_cycle(create_linked_list([1,2,3,4,5,2])) # -->> return reference to the node containing 2
start_of_cycle(create_linked_list([1,9,3,7,7])) # -->> return reference to node containing 7
