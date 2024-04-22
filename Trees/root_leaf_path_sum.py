# Given a binary tree and a target, return whether or not there exists a root to leaf path such that all values along the path sum to the target.

# Ex: Given the following tree…
#       1
#      / \
#     5   2
#    /   / \
#   1  12   29
# and a target of 15, return true as the path 1->2->12 sums to 15.
# Ex: Given the following tree…

#      104
#     /   \
#   39     31
#  / \    /  \
# 32  1  9    10
# and a target of 175, return true as the path 104->39->32 sums to 175.

class TreeNode():
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

def root_leaf_path_sum(root: TreeNode, target: int, path=[]):
    if root == None:
        return False
    
    path.append(root.value)
    
    if root.left == None and root.right == None:
        if sum(path) == target:
            path.pop()
            return True
        path.pop()
        return False
    
    left = root_leaf_path_sum(root.left, target, path)
    right = root_leaf_path_sum(root.right, target, path)
    
    path.pop()
    return left | right






# ====== Tests =======
a = TreeNode(1)
a.left = TreeNode(5)
a.right = TreeNode(2)
a.left.left = TreeNode(1)
a.right.left = TreeNode(12)
a.right.right = TreeNode(29)


b = TreeNode(104)
b.left = TreeNode(39)
b.right = TreeNode(31)
b.left.left = TreeNode(32)
b.left.right = TreeNode(1)
b.right.left = TreeNode(9)
b.right.right = TreeNode(10)

print(root_leaf_path_sum(a, 15)) # return true as the path 1->2->12 sums to 15
print(root_leaf_path_sum(b, 175)) # return true as the path 104->39->32 sums to 175