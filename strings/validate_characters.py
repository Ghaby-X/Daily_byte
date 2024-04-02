# This question is asked by Google. Given a string only containing the following characters (, ), {, }, [, and ] return whether or not the opening and closing characters are in a valid order.

# Ex: Given the following strings...

# "(){}[]", return true
# "(({[]}))", return true
# "{(})", return false

def validate(string: str):
    stack = []
    dictionary = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    
    for i in string:
        if i not in dictionary:
            stack.append(i)
            continue
            
        if dictionary[i] != stack[-1]:
            print('False')
            return
        
        stack.pop()
    
    if len(stack) == 0:
        print(True)
        return
    
    print(False)
    return

validate('(){}[]') # true
validate('(({[]}))') # true
validate('{(})') # false
validate('[()]{}{[()()]()}' ) # true