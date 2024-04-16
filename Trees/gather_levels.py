# Given a binary tree, return its level order traversal where the nodes in each level are ordered from left to right.

# Ex: Given the following tree...

#     4
#    / \
#   2   7
# return [[4], [2, 7]]
# Ex: Given the following tree...

#     2
#    / \
#   10  15
#         \
#          20
# return [[2], [10, 15], [20]]
# Ex: Given the following tree...

#     1
#    / \
#   9   32
#  /      \
# 3        78
# return [[1], [9, 32], [3, 78]]

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
def hash_to_list(hash: dict):
    if not hash: return
    
    list_of_levels = []
    
    for i in hash.values():
        list_of_levels.append(i)
    
    return list_of_levels

def hash_levels(root: TreeNode, lvl = 0, levels = dict()) -> None:
    if root == None:
        return


    if lvl in levels:
        levels[lvl].append(root.value)
    else:
        levels[lvl] = [ root.value ]
        
    hash_levels(root.left, lvl + 1, levels)
    hash_levels(root.right, lvl + 1, levels)

def gather_levels(root: TreeNode):
    hashed_levels = {}
    
    hash_levels(root, 0, hashed_levels)
    print(hash_to_list(hashed_levels))

# ======== Tests =========
a = TreeNode(4)
a.left = TreeNode(2)
a.right = TreeNode(7)

b = TreeNode(2)
b.left = TreeNode(10)
b.right = TreeNode(15)
b.right.right = TreeNode(20)

c = TreeNode(1)
c.left = TreeNode(9)
c.right = TreeNode(32)
c.left.left = TreeNode(3)
c.right.right = TreeNode(78)


gather_levels(a)
gather_levels(b)
gather_levels(c)
