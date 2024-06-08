# This question is asked by Apple. Given a list of positive numbers without duplicates and a target number, find all unique combinations of the numbers that sum to the target. Note: You may use the same number more than once.

# Ex: Given the following numbers and target…

# numbers = [2,4,6,3], target = 6,
# return [
#     [2,2,2],
#     [2,4],
#     [3,3],
#     [6]
# ]

def unique_combinations(numbers: list, target: int):
    answer = []
    check_set = []
    
    
    def recurse(numbers: list, target: int, output = []):
        if target == 0:
            sorted_output = sorted(output)
            if sorted_output in check_set:
                return
            
            answer.append(sorted_output)
            check_set.append(sorted_output)
            return
        
        if target < 0:
            return
        
            
        for i in numbers:
            output.append(i)
            recurse(numbers, target - i, output)
            output.pop()
    
    recurse(numbers, target)
    print(answer)

unique_combinations([2,4,6,3], 6)