# Given a binary tree, return its zig-zag level order traversal (i.e. its level order traversal from left to right the first level, right to left the level the second, etc.).

# Ex: Given the following tree…

#     1
#    / \
#   2   3
# return [[1], [3, 2]]
# Ex: Given the following tree…

#     8
#    / \
#   2  29
#     /  \
#    3    9
# return [[8], [29, 2], [3, 9]]

class TreeNode:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None
        
def zigzag_levels(root: TreeNode):
    if root == None: return
    
    queue = [ root ]
    zigzag = [[root.value]]
    
    flag = True # flag to indicate whether to reverse or not 
    
    while queue:
        current = queue.pop(0)
        temp = []
        
        if current.left:
            queue.append(current.left)
            temp.append(current.left.value)
            
        if current.right:
            queue.append(current.right)
            
            # insert right value to beginning or end of temp array depending on flag
            if not flag:
                temp.append(current.right.value)
                flag = True
            else:
                temp = [current.right.value] + temp
                flag = False
            
        
        if len(temp) > 0: zigzag.append(temp)
    
    print(zigzag)


# ===== Tests =======
a = TreeNode(1)
a.left = TreeNode(2)
a.right = TreeNode(3)

b = TreeNode(8)
b.left = TreeNode(2)
b.right = TreeNode(29)
b.right.left = TreeNode(3)
b.right.right = TreeNode(9)

# ========
zigzag_levels(a)
zigzag_levels(b)