# Given a binary tree, return a list of strings containing all root to leaf paths.

# Ex: Given the following tree…

#    1
#  /   \
# 2     3
# return ["1->2", "1->3"]
# Ex: Given the following tree…

#     8
#    / \
#   2  29
#     /  \
#    3    9
# return ["8->2", "8->29->3", "8->29->9"]

class TreeNode:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

def dfs(root: TreeNode, path = [], answer = []):
    if root == None:
        return
    
    # append current parent node to ancestor nodes of a particular leaf
    path.append( str(root.value) )
    
    # At the leaf of each node, answer append the path and remove last path
    if root.right == None and root.left == None:
        answer.append('->'.join(path))
        path.pop()
        return
    
    
    dfs(root.left, path, answer)
    dfs(root.right, path, answer)
    
    # Remove last path value when moving up the tree
    path.pop()
    
    
    
    pass


def root_to_leaf_path(root: TreeNode):
    answer = []
    
    dfs(root, answer=answer)
    print(answer)
    
    pass

# ====== tests ========
a = TreeNode(1)
a.left = TreeNode(2)
a.right = TreeNode(3)

b = TreeNode(8)
b.left = TreeNode(2)
b.right = TreeNode(29)
b.right.left = TreeNode(3)
b.right.right = TreeNode(9)

root_to_leaf_path(a) # return ["1->2", "1->3"]
root_to_leaf_path(b) # return ["8->2", "8->29->3", "8->29->9"]