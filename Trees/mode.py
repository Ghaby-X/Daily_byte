# Given a binary search tree, return its mode (you may assume the answer is unique). If the tree is empty, return -1. Note: the mode is the most frequently occurring value in the tree.

# Ex: Given the following tree...

#         2
#        / \
#       1   2
# return 2.

# Ex: Given the following tree...

#          7
#         / \
#       4     9
#      / \   / \
#     1   4 8   9
#                \
#                 9  
class TreeNode:
    def __init__(self, value) -> None:
        self.value = value
        self.right = None
        self.left = None

def inorder(root: TreeNode, hash = dict) -> None:
    if root == None:
        return
    
    inorder(root.left, hash)
    if root.value in hash:
        hash[root.value] += 1
    else:
        hash[root.value] = 1
    inorder(root.right, hash)

def mode(root: TreeNode):
    frequency_hash = {}
    
    # populate frequency hash with the freq of each node
    inorder( root, frequency_hash)
    
    mode = 0
    mode_key = 0
    
    # iterate through freq hash and return most frequent node
    for key in frequency_hash.keys():
        if frequency_hash[key] > mode:
            mode = frequency_hash[key]
            mode_key = key

    print(mode_key)


a = TreeNode(2)
a.left = TreeNode(1)
a.right = TreeNode(2)

b = TreeNode(7)
b.left = TreeNode(4)
b.left.left = TreeNode(1)
b.left.right = TreeNode(4)
b.right = TreeNode(9)
b.right.left = TreeNode(8)
b.right.right = TreeNode(9)
b.right.right.right = TreeNode(9)

mode(a) # return 2
mode(b) # return 9