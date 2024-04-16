# Given a binary tree, return the largest value in each of its levels. Ex: Given the following tree…

#     2
#    / \
#   10  15
#         \
#          20
# return [2, 15, 20]
# Ex: Given the following tree…

#           1
#          / \
#         5   6
#        / \   \  
#       5   3   7 
# return [1, 6, 7]
class TreeNode:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

def max_hash(root: TreeNode, lvl, levels: dict):
    if root == None: return
    
    if lvl in levels:
        levels[lvl] = max(levels[lvl], root.value)
    else:
        levels[lvl] = root.value
        
    max_hash(root.left, lvl + 1, levels)
    max_hash(root.right, lvl + 1, levels)

def max_values_in_levels(root: TreeNode):
    hashed_max = {}
    answer = []
    
    max_hash(root, 0, hashed_max)
    
    for i in hashed_max.values():
        answer.append(i)
    
    print(answer)

a = TreeNode(2)
a.left = TreeNode(10)
a.right = TreeNode(15)
a.right.right = TreeNode(20)

b = TreeNode(1)
b.left = TreeNode(5)
b.right = TreeNode(6)
b.left.left = TreeNode(5)
b.left.right = TreeNode(3)
b.right.right = TreeNode(7)

max_values_in_levels(a) # return [2, 15, 20]
max_values_in_levels(b) # return [1, 6, 7]