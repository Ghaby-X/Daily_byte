# # Given an array of numbers sorted in ascending order, return a height-balanced binary search tree using every number from the array.
# # Note: height-balanced meaning that the level of any node’s two subtrees should not differ by more than one.

# # Ex: Given the following nums...

# # nums = [1, 2, 3] return a reference to the following tree...
# #        2
# #       /  \
# #      1    3
# # Ex: Given the following nums...

# # nums = [1, 2, 3, 4, 5, 6] return a reference to the following tree...
# #         3
# #        / \
# #       2   5
# #      /   / \
# #     1   4   6


# # 2 1 3
# # 3 2 5 1 4 6

class TreeNode:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None




def convert(array: list):
    if len(array) == 0:
        return None
    
    if len(array) == 1:
        return TreeNode(array[0])
    

    middle_idx = len(array) // 2
    
    Node = TreeNode(array[middle_idx])
    Node.left = convert(array[:middle_idx])
    Node.right = convert(array[middle_idx + 1:])
    
    return Node

a = convert([1,2,3])
b = convert([1,2,3,4,5,6])



print(a.value)
print(a.left.value)
print(a.right.value)
print('------------------------')
print(b.value)
print(b.left.value)
print(b.right.value)
print(b.left.left.value)
print(b.left.right.value)
print(b.right.left.value)
