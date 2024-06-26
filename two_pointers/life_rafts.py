# This question is asked by Amazon. A ship is about to set sail and you are responsible for its safety precautions. More specifically, you are responsible for determining how many life rafts to carry onboard. You are given a list of all the passengers’ weights and are informed that a single life raft has a maximum capacity of limit and can hold at most two people. Return the minimum number of life rafts you must take onboard to ensure the safety of all your passengers. Note: You may assume that a the maximum weight of any individual is at most limit.

# Ex: Given the following passenger weights and limit…

# weights = [1, 3, 5, 2] and limit = 5, return 3
# weights = [1, 2] and limit = 3, return 1
# weights = [4, 2, 3, 3] and limit = 5 return 3


def max_raft(weights, limit):
    
    l = 0
    r = len(weights) - 1
    sort_weights = sorted(weights)
    min_number = 0
    
    while(l <= r):             
        if (sort_weights[r] + sort_weights[l]) <= limit:
            l += 1
        
        r -= 1
        min_number += 1

        
    
    print(min_number)
    

max_raft([1,3,5,2], 5)
max_raft([1,2], 3)
max_raft([4, 2, 3,5 ], 5)