# Given a binary search tree, rearrange the tree such that it forms a linked list where all its values are in ascending order.

# Ex: Given the following tree...
#         5
#        / \
#       1   6
# return...

# 1
#  \
#   5
#    \
#     6
# Ex: Given the following tree...

#        5
#       / \
#     2    9
#    / \ 
#   1   3 
# return...

# 1
#  \
#   2
#    \
#     3
#      \
#       5
#        \
#         9
# Ex: Given the following tree...

# 5
#  \
#   6
# return...

# 5
#  \
#   6

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None
        
class ListNode:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None
        
def printNodeChain(ptr):
    chain = []
    while (ptr is not None):
        chain.append(str(ptr.val))
        ptr = ptr.next
    
    chain.append('null')
    print(' -> '.join(chain))

def rearrange(node: Node):
    # answer = organize(node)
    # printNodeChain(answer.next)
    
    answer = organize(node) # returns [(-1 -> headNode), tailNode]
    printNodeChain(answer[0].next)

def organize(node: Node):
    if node == None:
        value = ListNode(-1)
        return [value, value] # returns [(-1 -> headNode), tailNode]
       
    leftValue = organize(node.left)
    rightValue = organize(node.right)
    
    tailNode = leftValue[1] # get tailNode of left linked list
    tailNode.next = ListNode(node.value) # append new Node to tail
    tailNode.next.next = rightValue[0].next # append right LinkedList to after tail
    
    #updating tailNode
    if (tailNode.next.next):
        tailNode = tailNode.next.next
    else:
        tailNode = tailNode.next
    
    return [leftValue[0], tailNode] # returns [(-1 -> headNode), tailNode]


## =================== Tests ====================

# ===== defining tree structure =====

# Node 1
#         5
#        / \
#       1   6
node1 = Node(5)
node1.left = Node(1)
node1.right = Node(6)


# Node 2
#        5
#       / \
#     2    9
#    / \ 
#   1   3 

node2 = Node(5)
node2.left = Node(2)
node2.left.left = Node(1)
node2.left.right = Node(3)
node2.right = Node(9)

# Node 3
# 5
#  \
#   6

node3 = Node(5)
node3.right = Node(6)



# === running functions ===

rearrange(node1) # return 1 -> 5 -> 6 -> null
rearrange(node2) # return 1 -> 2 -> 3 -> 5 -> 9 -> null
rearrange(node3) # return 5 -> 6 -> null