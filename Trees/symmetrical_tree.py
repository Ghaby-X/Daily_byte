# Given a binary tree, return whether or not it forms a reflection across its center (i.e. a line drawn straight down starting from the root).
# Note: a reflection is when an image, flipped across a specified line, forms the same image.

# Ex: Given the following tree…

#    2
#  /   \
# 1     1
# return true as when the tree is reflected across its center all the nodes match.
# Ex: Given the following tree…

#     1
#    / \
#   5   5
#    \    \
#     7    7
# return false as when the tree is reflected across its center the nodes containing sevens do not match.

class TreeNode:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None
        
def symmetrical_tree(root: TreeNode):
    if root == None:
        return True
    
    if root.left and root.right and root.left.value != root.right.value:
        return False
    
    if (root.left and root.right == None) or (root.right and root.left == None):
        return False
        
    left = symmetrical_tree(root.left)
    right = symmetrical_tree(root.right)
    
    return left & right

# ====== Tests ========
a = TreeNode(2)
a.left = TreeNode(1)
a.right = TreeNode(1)

b = TreeNode(1)
b.left = TreeNode(5)
b.right = TreeNode(5)
b.left.right = TreeNode(7)
b.right.right = TreeNode(7)


print(symmetrical_tree(a))
print(symmetrical_tree(b))
