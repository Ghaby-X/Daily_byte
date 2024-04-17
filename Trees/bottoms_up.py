# Given a binary tree, returns of all its levels in a bottom-up fashion (i.e. last level towards the root). Ex: Given the following tree…

#         2
#        / \
#       1   2
# return [[1, 2], [2]]
# Ex: Given the following tree…

#        7
#       / \
#     6    2
#    / \ 
#   3   3 
# return [[3, 3], [6, 2], [7]]
class TreeNode:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

def group_levels(root: TreeNode, lvl: int, levels: dict):
    if root == None: return
    
    if lvl in levels:
        levels[lvl].append(root.value)
    else:
        levels[lvl] = [ root.value ]
        
    group_levels(root.left, lvl + 1, levels)
    group_levels(root.right, lvl + 1, levels)


def bottoms_up(root: TreeNode):
    levels = {}
    group_levels(root, 0, levels)
    
    answer = list(levels.values())[::-1]
    print(answer)


# ======== Tests ==========
a = TreeNode(2)
a.left = TreeNode(1)
a.right = TreeNode(2)


b = TreeNode(7)
b.left = TreeNode(6)
b.right = TreeNode(2)
b.left.left = TreeNode(3)
b.left.right = TreeNode(3)

bottoms_up(a) # return [[1, 2], [2]]
bottoms_up(b) # return [[3, 3], [6, 2], [7]]