# Given two binary trees, return whether or not the two trees are identical. Note: identical meaning they exhibit the same structure and the same values at each node. Ex: Given the following trees...

#         2
#        / \
#       1   3
#     2
#    / \
#   1   3

# return true.

# Ex: Given the following trees...

#         1
#          \
#           9
#            \
#            18
#     1
#    /
#   9
#    \
#     18

# return false.

# Ex: Given the following trees...

#         2
#        / \
#       3   1
#     2
#    / \
#   1   3

# return false. 

class TreeNode:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None



def is_identical(root1: TreeNode, root2: TreeNode):
    # if both roots are None
    if root1 == None and root2 == None:
        return True
    
    # if both roots contain a value and their child are equal
    if root1 != None and root2 != None:
        return (
            (root1.value == root2.value) and
            (is_identical(root1.left, root2.left)) and
            (is_identical(root1.right, root2.right))
        )
    
    #if one node is none and the other is not
    return False


# ============= Tests ================

# == case 1 ==
r1 = TreeNode(2)
r1.left = TreeNode(1)
r1.right = TreeNode(3)

r2 = TreeNode(2)
r2.left = TreeNode(1)
r2.right = TreeNode(3)


# == Case 2 ==
r3 = TreeNode(1)
r3.right = TreeNode(9)
r3.right.right = TreeNode(18)

r4 = TreeNode(1)
r4.left = TreeNode(9)
r4.left.right = TreeNode(18)

# == case 3 == 
r5 = TreeNode(2)
r5.left = TreeNode(3)
r5.right = TreeNode(1)

r6 = TreeNode(2)
r6.right = TreeNode(3)
r6.left = TreeNode(1)

print(is_identical(r1, r2)) # True
print(is_identical(r3, r4)) # False
print(is_identical(r5, r6)) # False