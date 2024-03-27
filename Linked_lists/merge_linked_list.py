# This question is asked by Apple. Given two sorted linked lists, merge them together in ascending order and return a reference to the merged list

# Ex: Given the following lists...

# list1 = 1->2->3, list2 = 4->5->6->null, return 1->2->3->4->5->6->null
# list1 = 1->3->5, list2 = 2->4->6->null, return 1->2->3->4->5->6->null
# list1 = 4->4->7, list2 = 1->5->6->null, return 1->4->4->5->6->7->null

from Linked_List import LinkedList, create_linked_list, Node
def merge(l1, l2):
    answer = Node(4)
    ans_pointer = answer
    
    l1_current = l1.head
    l2_current = l2.head
    
    while(True):
        if l1_current is None:
            ans_pointer.next = l2_current
            break
        
        if l2_current is None:
            ans_pointer.next = l1_current
            break
        
        if l1_current.val < l2_current.val:
            ans_pointer.next = l1_current
            l1_current = l1_current.next
        else:
            ans_pointer.next = l2_current
            l2_current = l2_current.next
        
        ans_pointer = ans_pointer.next
    
    def print_values(headNode):
        lst = []
        cur = headNode
        while cur:
            lst.append(str(cur.val))
            cur = cur.next
        
        if len(lst) == 0:
            print('null')
            return
        
        print(' -> '.join(lst) + ' -> null')
    
    print_values(answer.next)
    return


merge(create_linked_list([1,2,3]), create_linked_list([4,5,6]))   #  1->2->3->4->5->6->null
merge(create_linked_list([1,3, 5]), create_linked_list([2,4,6]))  #  1->2->3->4->5->6->null
merge(create_linked_list([4,4,7]), create_linked_list([1,5,6]))   #  1->4->4->5->6->7->null