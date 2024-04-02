# This question is asked by Microsoft. Given a linked list, containing unique numbers, return whether or not it has a cycle.
# Note: a cycle is a circular arrangement (i.e. one node points back to a previous node)

# Ex: Given the following linked lists...

# 1->2->3->1 -> true (3 points back to 1)
# 1->2->3 -> false
# 1->1 true (1 points to itself)




from Linked_List import Node

def contains_cycle(lst):
    fast = lst
    slow = lst
    
    while(fast and fast.next):
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            print(True)
            return
    
    print(False)
    return


lst1 = Node(1)
lst1.next = Node(2)
lst1.next.next = Node(3)
lst1.next.next.next = lst1

lst2 = Node(1)
lst2.next = Node(2)
lst2.next.next = Node(3)

lst3 = Node(1)
lst3.next = lst3


contains_cycle(lst1) # true
contains_cycle(lst2) # false
contains_cycle(lst3) # true