# Given a binary tree, return its column order traversal from top to bottom and left to right. Note: if two nodes are in the same row and column, order them from left to right.

# Ex: Given the following tree…

#     8
#    / \
#   2   29
#      /  \
#     3    9
# return [[2], [8, 3], [29], [9]]
# Ex: Given the following tree…

#      100
#     /   \
#   53     78
#  / \    /  \
# 32  3  9    20
# return [[32], [53], [100, 3, 9], [78], [20]]

class TreeNode:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

# returns a hashmap of column level and the respective nodes in each column
# the column containing the rootNode is zero, columns to the immediate left of the root is -1.
# columns decrease by 1 as you move farther left from the root
# column to the immediate right is 1
# columns increase by 1 as you move farther left from the root
def column_hash(root: TreeNode, col, columns):
    if root == None: return
    
    if col in columns:
        columns[col].append(root.value)
    else:
        columns[col] = [ root.value ]
    
    column_hash(root.left, col - 1, columns)
    column_hash(root.right, col + 1, columns)

def gather_columns(root: TreeNode):
    columns = {}
    answer = []
    
    column_hash(root, 0, columns)
    
    # display the columns from left to right, and in a list format
    sorted_keys = sorted(columns.keys())
    
    for i in sorted_keys:
        answer.append(columns[i])
    
    print(answer)
    
    
    
    
# ======= Tests =======
a = TreeNode(8)
a.left = TreeNode(2)
a.right = TreeNode(29)
a.right.left = TreeNode(3)
a.right.right = TreeNode(9)

b = TreeNode(100)
b.left = TreeNode(53)
b.right = TreeNode(78)
b.left.left = TreeNode(32)
b.left.right = TreeNode(3)
b.right.left = TreeNode(9)
b.right.right = TreeNode(20)

gather_columns(a) # return [[2], [8, 3], [29], [9]]
gather_columns(b) # return [[32], [53], [100, 3, 9], [78], [20]]