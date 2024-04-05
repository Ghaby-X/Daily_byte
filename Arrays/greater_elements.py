# This question is asked by Amazon. Given two arrays of numbers, where the first array is a subset of the second array, return an array containing all the next greater elements for each element in the first array, in the second array. If there is no greater element for any element, output -1 for that number.

# Ex: Given the following arrays…

# nums1 = [4,1,2], nums2 = [1,3,4,2], return [-1, 3, -1] because no element in nums2 is greater than 4, 3 is the first number in nums2 greater than 1, and no element in nums2 is greater than 2.
# nums1 = [2,4], nums2 = [1,2,3,4], return [3, -1] because 3 is the first greater element that occurs in nums2 after 2 and no element is greater than 4.


# def greater_element(arr1: list, arr2: list):
#     answer = []
#     for i in arr1:
#         hasgreater = False
#         idx = arr2.index(i)
        
#         for j in range(idx, len(arr2)):
#             if arr2[j] > i:
#                 hasgreater = True
#                 answer.append(arr2[j])
#                 break
            
#         if hasgreater == False:
#             answer.append(-1)
    
#     print(answer)
#     return

def greater_element(arr1: list, arr2: list):
    cache, st = {}, []
    
    for i in arr2:
        while st and st[-1] < i:
            cache[st.pop()] = i
        st.append(i)
        
    answer = []
    
    for i in arr1:
        if i in cache:
            answer.append(cache[i])
        else:
            answer.append(-1)
    
    print(answer)
    return

#tests
greater_element([4,1,2], [1,3,4,2]) # return [-1, 3, -1]
greater_element([2, 4], [1,2,3,4]) # return [3, -1]
