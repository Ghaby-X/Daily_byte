# This question is asked by Amazon. Given a string s consisting of only letters and digits, where we are allowed to transform any letter to uppercase or lowercase, return a list containing all possible permutations of the string.

# Ex: Given the following string…

# S = "c7w2", return ["c7w2", "c7W2", "C7w2", "C7W2"]

# def permute(s: str):
#     result = []
    
#     def backtrack(output: list, i):
#         if i >= len(s):
#             result.append("".join(output))
#             return
        
#         char = s[i]
#         if char.isalpha():
#             # Handle lower case
#             output.append(char.lower())
#             backtrack(output, i+1)
#             output.pop()
            
#             # Handle upper case
#             output.append(char.upper())
#             backtrack(output, i+1)
#             output.pop()
            
#         elif char.isdigit():
#             output.append(char)
#             backtrack(output, i+1)
#             output.pop()
    
#     backtrack([], 0)
#     print(result)


def permute(string):
    result = []
    
    
    def backtrack(string, out: list):
        if len(string) == 0:
            result.append("".join(out))
            return 
    
        char: str = string[0]
        if char.isalpha():
            alpha = [ char.upper(), char.lower()]
            for c in alpha:
                out.append(c)
                backtrack(string[1:], out)
                out.pop()
                
        else:
            out.append(char)
            backtrack(string[1:], out)
            out.pop()

        
    backtrack(string, [])
    print(result)
    pass

# =================
string = 'c7w2'
permute(string)