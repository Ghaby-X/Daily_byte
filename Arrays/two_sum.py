# This question is asked by Google. Given an array of integers, return whether or not two numbers sum to a given target, k.
# Note: you may not sum a number with itself.

# Ex: Given the following...

# [1, 3, 8, 2], k = 10, return true (8 + 2)
# [3, 9, 13, 7], k = 8, return false
# [4, 2, 6, 5, 2], k = 4, return true (2 + 2)


def two_sum( A: list[int], k: int):
    library = set()
    
    for i in A:
        if i in library:
            print(True)
            return
        
        library.add(k-i)
    
    print(False)
    return

#tests
two_sum([1, 3, 8, 2], 10) # ->> true
two_sum([3, 9, 13, 7], 8) # ->> false
two_sum([4, 2, 6, 5, 2], 4) # ->> true