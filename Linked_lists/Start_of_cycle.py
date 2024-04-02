# This question is asked by Apple. Given a potentially cyclical linked list where each value is unique, return the node at which the cycle starts. If the list does not contain a cycle, return null.

# Ex: Given the following linked lists...

# 1->2->3, return null
# 1->2->3->4->5->2 (5 points back to 2), return a reference to the node containing 2
# 1->9->3->7->7 (7 points to itself), return a reference to the node containing 7

from Linked_List import create_linked_list, Node

def start_of_cycle(lst):
    cycle_start_reference = None
    current = lst
    
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

def floyd_cycle_algorithm(lst):
    
    slow = lst
    fast = lst
    
    while(fast != None and fast.next != None):
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            break
    
    if slow != fast:
        print('None')
        return
    
    slow = lst
    
    while(slow, fast and fast.next):
        if slow == fast:
            cycle_start = slow
            print(cycle_start.val)
            return
        
        slow = slow.next
        fast = fast.next
        
    pass


#testss
lst1 = Node(1)
lst1.next = Node(2)
lst1.next.next = Node(3)

lst2 = Node(1)
lst2.next = Node(2)
lst2.next.next = Node(3)
lst2.next.next.next = Node(4)
lst2.next.next.next.next = Node(5)
lst2.next.next.next.next.next = lst2.next

lst3 = Node(1)
lst3.next = Node(9)
lst3.next.next = Node(3)
lst3.next.next.next = Node(7)
lst3.next.next.next.next = lst3.next.next.next


start_of_cycle(lst1) # -->> return null
start_of_cycle(lst2) # -->> return reference to the node containing 2
start_of_cycle(lst3)# -->> return reference to node containing 73)



floyd_cycle_algorithm(lst1) # -->> return null
floyd_cycle_algorithm(lst2) # -->> return reference to the node containing 2
floyd_cycle_algorithm(lst3) # -->> return reference to node containing 7
