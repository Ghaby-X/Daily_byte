# This question is asked by Google. Given a string, return whether or not it uses capitalization correctly. A string correctly uses capitalization if all letters are capitalized, no letters are capitalized, or only the first letter is capitalized.

# Ex: Given the following strings...

# "USA", return true
# "Calvin", return true
# "compUter", return false
# "coding", return true

def is_correctly_capitalized(s:str):
    length = len(s)
    if s == '':
        print(True)
        return
    
    is_first_capital = s[0].isupper()
    
    if is_first_capital == True:
        #check second
        is_second_capital = s[1].isupper()
        
        if is_second_capital:
            for i in range(2, length):
                if s[i].islower():
                    print(False)
                    return
        else:
            for i in range(2, length):
                if s[i].isupper():
                    print(False)
                    return
    else:
        for i in range(2, length):
            if s[i].isupper():
                print(False)
                return
    
    print(True)
    return

#tests
is_correctly_capitalized("USA") # ->> True
is_correctly_capitalized("Calvin") # ->> True
is_correctly_capitalized("compUter") # ->> False
is_correctly_capitalized("coding") # ->> True