# This question is asked by Facebook. Given an integer N, where N represents the number of pairs of parentheses (i.e. ”(“ and ”)”) you are given, return a list containing all possible well-formed parentheses you can create.

# Ex: Given the following value of N…

# N = 3, 
# return [  
#     "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]

def generate_parentheses(N: int):
    answer = []
    
    def populate(open = 1, close= 0, output = '('):
        if len(output) == 2*N:
            answer.append(output)
            return
        
        if open < N:
            populate(open + 1, close, output + '(')
            
        if close < open:
            populate(open, close + 1, output + ')')
            

    
    populate()
    print(answer)

generate_parentheses(3)