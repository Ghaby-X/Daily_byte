# This question is asked by Google. Given the reference to the root of a binary search tree and a search value, return the reference to the node that contains the value if it exists and null otherwise.
# Note: all values in the binary search tree will be unique.

# Ex: Given the tree...

#         3
#        / \
#       1   4
# and the search value 1 return a reference to the node containing 1.
# Ex: Given the following tree...

#         7
#        / \
#       5   9
#          / \ 
#         8   10
# and the search value 9 return a reference to the node containing 9.
# Ex: Given the following tree...

#         8
#        / \
#       6   9
# and the search value 7 return null.

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

def FindValue(Node, reference, guide=[]):
    if Node.value == reference:
        guide.append('value')
        print('found at: ', 'head -> ' + ''.join(guide))
        return Node
    
    if Node.value > reference:
        guide.append(' left -> ')
        if Node.left is None:
            guide.append(' None ')
            return None
        return FindValue(Node.left, reference, guide)
    else:
        guide.append(' right -> ')
        if Node.right is None:
            guide.append(' None ')
            return None
        return FindValue(Node.right, reference, guide)

node1 = Node(3)
node1.left = Node(1)
node1.right = Node(4)

#         7
#        / \
#       5   9
#          / \ 
#         8   10
node2 = Node(7)
node2.left = Node(5)
node2.right = Node(9)
node2.right.left = Node(8)
node2.right.right = Node(10)


#         8
#        / \
#       6   9
node3 = Node(3)
node3.left = Node(6)
node3.right = Node(9)

FindValue(node1, 1, [])
print( ' -------------------------------------------------')
FindValue(node2, 10, [])
print( ' -------------------------------------------------')
FindValue(node3, 7, [])
print( '-------------------------------------------------')