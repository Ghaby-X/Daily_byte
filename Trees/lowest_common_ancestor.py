# Given a binary search tree that contains unique values and two nodes within the tree, a, and b, return their lowest common ancestor.
# Note: the lowest common ancestor of two nodes is the deepest node within the tree such that both nodes are descendants of it.

# Ex: Given the following tree...
#        7
#       / \
#     2    9
#    / \ 
#   1   5 
# and a = 1, b = 9, return a reference to the node containing 7.
# Ex: Given the following tree...

#         8
#        / \
#       3   9
#      / \ 
#     2   6
# and a = 2, b = 6, return a reference to the node containing 3.
# Ex: Given the following tree...

#         8
#        / \
#       6   9
# and a = 6, b = 8, return a reference to the node containing 8.

# === defining structure for treeNode
class TreeNode:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

# === finds whether a given tree contains a value
def contains_value(node: TreeNode, val: int):
    if node == None:
        return False
    
    if node == val:
        return True
    
    return contains_value(node.left, val) | contains_value(node.right, val)

# === returns the node of the first target value, it's immediate parent, and the other target value
def immediate_parent(node: TreeNode, a: int, b: int):
    if node == None: return None
    if node.value == a:
        return node, node, b
    if node.value == b:
        return node, node, a
    queue = [ node ]
    
    while queue: 
        currentNode = queue.pop(0)
        
        if currentNode.left: 
            if currentNode.left.value == a:
                return currentNode, currentNode.left, b
            if currentNode.left.value == b:
                return currentNode, currentNode.left, a
            
            queue.append(currentNode.left)
        
        if currentNode.right: 
            if currentNode.right.value == a:
                return currentNode, currentNode.right, b
            if currentNode.right.value == b:
                return currentNode, currentNode.right, a
            
            queue.append(currentNode.right)
    
    return None, None, None

# === finds lowest_common_ancestor 
def lowest_common_ancestor(node: TreeNode, a: int, b: int):
    parentNode, valueNode, val = immediate_parent(node, a, b)
    
    if parentNode == None or valueNode == None:
        print('didnt find one')
        return None
    
    is_present = contains_value(valueNode, val)
    
    if is_present:
        print(valueNode.value)
        return valueNode
    else:
        print(parentNode.value)
        return parentNode



# ================= Tests ==================

#         8
#        / \
#       6   9
# and a = 6, b = 8, return a reference to the node containing 8.

a = TreeNode(8)
a.left = TreeNode(6)
a.right = TreeNode(9)


#         8
#        / \
#       3   9
#      / \ 
#     2   6
# and a = 2, b = 6, return a reference to the node containing 3.

b = TreeNode(8)
b.right = TreeNode(9)
b.left = TreeNode(3)
b.left.left = TreeNode(2)
b.left.right = TreeNode(6)

#        7
#       / \
#     2    9
#    / \ 
#   1   5 
# and a = 1, b = 9, return a reference to the node containing 7.

c = TreeNode(7)
c.left = TreeNode(2)
c.right = TreeNode(9)
c.left.left = TreeNode(1)
c.left.right = TreeNode(5)

lowest_common_ancestor(a, 6, 8)
lowest_common_ancestor(b, 2, 6)
lowest_common_ancestor(c, 1, 7)