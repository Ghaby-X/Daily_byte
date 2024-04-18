# Given an n-ary tree, return its level order traversal.
# Note: an n-ary tree is a tree in which each node has no more than N children.

# Ex: Give the following n-ary tree…

#     8
#   / | \
#  2  3  29
# return [[8], [2, 3, 29]]
# Ex: Given the following n-ary tree…

#      2
#    / | \
#   1  6  9
#  /   |   \
# 8    2    2
#    / | \
#  19 12 90
# return [[2], [1, 6, 9], [8, 2, 2], [19, 12, 90]]

class TreeNode:
    def __init__(self, value) -> None:
        self.value = value
        self.children = []


# store all the nodes of each level in a dictionary called levels
def gather_levels(root: TreeNode, lvl: int, levels: dict):
    if root == None: return
    
    if lvl in levels:
        levels[lvl].append(root.value)
    else:
        levels[lvl] = [ root.value ]
        
    for c in root.children:
        gather_levels(c, lvl + 1, levels)
    
# print out the levels
def n_ary_levels(root: TreeNode):
    levels = {}
    
    gather_levels(root, 0, levels)
    print(levels)
    
# ======= Tests =======
a = TreeNode(6)
a.children = [TreeNode(2) , TreeNode(3), TreeNode(29)]

b = TreeNode(2)
b.children = [TreeNode(1), TreeNode(6), TreeNode(9)]
b.children[0].children = [TreeNode(8)]
b.children[1].children = [TreeNode(2)]
b.children[2].children = [TreeNode(2)]
b.children[1].children[0].children = [TreeNode(19), TreeNode(12), TreeNode(90)]

n_ary_levels(a) # return [[8], [2, 3, 29]]
n_ary_levels(b) # return [[2], [1, 6, 9], [8, 2, 2], [19, 12, 90]]