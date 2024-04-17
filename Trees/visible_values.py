# Given a binary tree return all the values you’d be able to see if you were standing on the left side of it with values ordered from top to bottom.

# Ex: Given the following tree…

# -->    4
#       / \
# -->  2   7
# return [4, 2]
# Ex: Given the following tree…

# -->        7
#          /  \
# -->     4     9
#        / \   / \
# -->   1   4 8   9
#                  \
# -->               9
# return [7, 4, 1, 9]

class TreeNode:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None
        
def hash_first_in_level(root: TreeNode, lvl: int, levels: dict):
    if root == None: return
    
    if lvl not in levels:
        levels[lvl] = root.value
        
    hash_first_in_level(root.left, lvl + 1, levels)
    hash_first_in_level(root.right, lvl + 1, levels)

def visible_values(root: TreeNode):
    levels = {}
    
    hash_first_in_level(root, 0, levels)
    print(levels.values())




# =========== Tests ============
a = TreeNode(4)
a.left = TreeNode(2)
a.right = TreeNode(7)

b = TreeNode(7)
b.left = TreeNode(4)
b.right = TreeNode(9)
b.left.left = TreeNode(1)
b.left.right = TreeNode(4)
b.right.left = TreeNode(8)
b.right.right = TreeNode(9)
b.right.right.right = TreeNode(9)

visible_values(a) # return [4, 2]
visible_values(b) # return [7, 4, 1, 9]