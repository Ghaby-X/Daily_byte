# Given a binary tree, return the sum of all left leaves of the tree. Ex: Given the following tree…

#     5
#    / \
#   2   12
#      /  \
#     3    8
# return 5 (i.e. 2 + 3)
# Ex: Given the following tree…

#        2
#       / \
#     4    2
#    / \ 
#   3   9 
# return 3

class TreeNode:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None
        
def get_left_nodes(root, isLeft = False, array = []):
    if root == None:
        return
    
    if root.right == None and root.left == None:
        if (isLeft):
            array.append(root.value)
        return

    get_left_nodes(root.left, True, array)
    get_left_nodes(root.right, False, array)
    

def sum_left_nodes(root):
    left_nodes = []
    
    get_left_nodes(root, array=left_nodes)
    print(sum(left_nodes))


# === Tests ====
a = TreeNode(5)
a.left = TreeNode(2)
a.right = TreeNode(12)
a.right.left = TreeNode(3)
a.right.right = TreeNode(8)

b = TreeNode(2)
b.left = TreeNode(4)
b.left.left = TreeNode(3)
b.left.right = TreeNode(9)
b.right = TreeNode(2)

# ===============
sum_left_nodes(a) # return 5
sum_left_nodes(b) # return 3