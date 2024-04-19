# Given a binary tree, return its maximum depth.
# Note: the maximum depth is defined as the number of nodes along the longest path from root node to leaf node.

# Ex: Given the following tree…

#     9
#    / \
#   1   2
# return 2
# Ex: Given the following tree…

#     5
#    / \
#   1  29
#     /  \
#    4   13
# return 3

class TreeNode:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None
        
def calculate_depth(root: TreeNode):
    if root == None:
        return 0
    
    left_depth = calculate_depth(root.left) + 1
    right_depth = calculate_depth(root.right) +  1
    
    if left_depth > right_depth:
        return left_depth
    else:
        return right_depth


# ======== Tests ==========
a = TreeNode(9)
a.left = TreeNode(1)
a.right = TreeNode(2)

b = TreeNode(5)
b.left = TreeNode(1)
b.right = TreeNode(29)
b.right.left = TreeNode(4)
b.right.right = TreeNode(13)


a_depth = calculate_depth(a) # return 2
print(a_depth)
b_depth = calculate_depth(b) # return 3
print(b_depth)