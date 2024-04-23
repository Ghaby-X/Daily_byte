# Given a binary tree, containing unique values, determine if it is a valid binary search tree.
# Note: the invariants of a binary search tree (in our case) are all values to the left of a given node are less than the current node’s value, all values to the right of a given node are greater than the current node’s value, and both the left and right subtrees of a given node must also be binary search trees.

# Ex: Given the following binary tree…

#    1
#  /   \
# 2     3
# return false.
# Ex: Given the following tree…

#    2
#  /   \
# 1     3
# return true.

class TreeNode:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None
        
def validate_tree(root: TreeNode):
    if root == None:
        return True
    
    if root.left == None and root.right == None:
        return True
    
    
    # if root.left & root.right == None:
    #     return root.value >= root.left.value
    
    # if root.right & root.left == None:
    #     return root.value <= root.right.value
    
    # if root.left != None and root.right != None:
    #     return root.value >= root.left.value & root.value <= root.right.value
    
    # left = validate_tree(root.left)
    # right = validate_tree(root.right)
    
def bfs_validate(root: TreeNode):
    if root == None: return True
    
    queue = [ root ]
    
    while queue:
        current = queue.pop(0)
        
        if current.left:
            if current.left.value > current.value:
                return False
            queue.append(current.left)
            
        if current.right:
            if current.right.value < current.value:
                return False
            queue.append(current.right)
    
    return True
    
    

# ==== Tests =====
a = TreeNode(1)
a.left = TreeNode(2)
a.right = TreeNode(3)

b = TreeNode(2)
b.left = TreeNode(1)
b.right = TreeNode(3)

print(bfs_validate(a)) # return false.
print(bfs_validate(b)) # return true.
    