# Given a binary search tree, return the minimum difference between any two nodes in the tree.

# Ex: Given the following tree...
#         2
#        / \
#       1   3
# return 1.
# Ex: Given the following tree...
#         29
#        /  \
#      17   50
#     /     / \
#    1    42  59
# return 8.
# Ex: Given the following tree...
#         2
#          \
#          100
# return 98.

class TreeNode:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

def minimum_difference(root: TreeNode):
    sorted_nodes = []
    inorder_traversal(root, sorted_nodes)
    
    differences = []
    
    for i in range(0,len(sorted_nodes) - 1):
        differences.append(sorted_nodes[i + 1] - sorted_nodes[i])
        
    print(min(differences))
    
def inorder_traversal(root: TreeNode, answer: list):
    if root == None:
        return
    
    inorder_traversal(root.left, answer)
    answer.append(root.value)
    inorder_traversal(root.right, answer)
    
    

# ======= tests ========
a = TreeNode(2)
a.left = TreeNode(1)
a.right = TreeNode(3)



b = TreeNode(29)
b.left = TreeNode(17)
b.right = TreeNode(50)
b.left.left = TreeNode(1)
b.right.left = TreeNode(42)
b.right.right = TreeNode(59)

c = TreeNode(2)
c.right = TreeNode(100)

minimum_difference(a) # return 1
minimum_difference(b) # return 8
minimum_difference(c) # return 98