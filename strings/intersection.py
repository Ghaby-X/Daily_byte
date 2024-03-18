# This question is asked by Google. Given two integer arrays, return their intersection.
# Note: the intersection is the set of elements that are common to both arrays.

# Ex: Given the following arrays...

# nums1 = [2, 4, 4, 2], nums2 = [2, 4], return [2, 4]
# nums1 = [1, 2, 3, 3], nums2 = [3, 3], return [3]
# nums1 = [2, 4, 6, 8], nums2 = [1, 3, 5, 7], return []

def intersection_of(a: list, b:list):
    intersection = []
    #get shortest array
    if len(a) > len(b):
        short = b
        long = a
    else:
        long = b
        short = a
        
    short = list(set(short))
    
    for i in short:
        if i in long:
            intersection.append(i)
        
    print(intersection)

#test
intersection_of([2, 4, 4, 2], [2, 4])
intersection_of([1, 2, 3, 3], [3,3])
intersection_of([2,4,6,8], [1,3,5,7])