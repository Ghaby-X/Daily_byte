# This question is asked by Facebook. Given a string s containing only lowercase letters, continuously remove adjacent characters that are the same and return the result.

# Ex: Given the following strings...

# s = "abccba", return ""
# s = "foobar", return "fbar"
# s = "abccbefggfe", return "a"


def filter(s: str):
    if len(s) == 1:
        print(s)
        return
    
    stack = []
    
    for i in s:
        if stack and i == stack[-1]:
            stack.pop()
            continue
        
        stack.append(i)
        
    print( ''.join(stack))
    return

#tests
filter('abccba') # return ""
filter('foobar') # return "fbar"
filter('abccbefggfe') # return "a"
