#creating linked list
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
        
    def addNode(self, val):
        if self.head is None:
            self.head = Node(val)
            self.size += 1
            return
        else:
            new_node = Node(val)
            new_node.next = self.head
            self.head = new_node
            self.size += 1
            return
   
     
    def printList(self):
        if self.head is None:
            print('Empty list')
            return
        else:
            lst = []
            current = self.head
            
            while current != None:
                lst.append(str(current.val))
                current = current.next
            
            print(' -> '.join(lst) + ' -> null')
            return

def create_linked_list(val: list):
    created_list = LinkedList()
    val = val[::-1]
    for i in val:
        created_list.addNode(i)
        
    return created_list

def print_node_chain(headNode):
        lst = []
        cur = headNode
        while cur:
            lst.append(str(cur.val))
            cur = cur.next
        
        if len(lst) == 0:
            print('null')
            return
        
        print(' -> '.join(lst) + ' -> null')