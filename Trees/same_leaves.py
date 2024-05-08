# Given two binary trees, return whether or not both trees have the same leaf sequence. Two trees have the same leaf sequence if both trees’ leaves read the same from left to right.

# Ex: Given the following trees…

#    1
#  /   \
# 1     3
# and


#    7
#  /   \
# 1     2
# return false as both the trees' leaves don't read the same from left to right (i.e. [1, 3] and [1, 2]).

# Ex: Given the following trees…

#     8
#    / \
#   2   29
#     /  \
#    3    9
# and

#     8
#    / \
#   2  29
#  /   /  \
# 2   3    9
#      \
#       3
# return true as both the trees' leaves read the same from left to right (i.e. [2, 3, 9] and [2, 3, 9]).

class TreeNode:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None
        
def get_leaves(root, array = []):
    if root == None:
        return
    
    if root.left == None and root.right == None:
        array.append(root.value)
        return
    
    get_leaves(root.left, array)
    get_leaves(root.right, array)

def is_same_leaves(root1, root2):
    root1_array = []
    root2_array = []
    
    get_leaves(root1, root1_array)
    get_leaves(root2, root2_array)
    
    print(root1_array == root2_array)
    pass

# ==== TESTS ====
a = TreeNode(1)
a.left = TreeNode(1)
a.right = TreeNode(3)

a_comp = TreeNode(7)
a_comp.left = TreeNode(1)
a_comp.right = TreeNode(2)

b = TreeNode(8)
b.left = TreeNode(2)
b.right = TreeNode(29)
b.right.left = TreeNode(3)
b.right.right = TreeNode(9)

b_comp = TreeNode(8)
b_comp.left = TreeNode(2)
b_comp.left.left = TreeNode(2)
b_comp.right = TreeNode(29)
b_comp.right.left = TreeNode(3)
b_comp.right.right = TreeNode(9)
b_comp.right.left.right = TreeNode(3)


# ==== ======
is_same_leaves(a, a_comp) # return false
is_same_leaves(b, b_comp) # return true