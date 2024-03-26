# This question is asked by Facebook. Given a string and the ability to delete at most one character, return whether or not it can form a palindrome.
# Note: a palindrome is a sequence of characters that reads the same forwards and backwards.

# Ex: Given the following strings...

# "abcba", return true
# "foobof", return true (remove the first 'o', the second 'o', or 'b')
# "abccab", return false

def valid_palidrome_with_removal(s: str):
    right_pointer = len(s) - 1
    left_pointer = 0
    removed = 0
    answer = True
    
    while right_pointer > left_pointer:
        if s[left_pointer] == s[right_pointer]:
            left_pointer += 1
            right_pointer -= 1
        else:
            if s[right_pointer - 1 ] == s[left_pointer]:
                right_pointer -= 1
            else:
                left_pointer += 1
            removed += 1
            if removed > 1:
                answer = False
                break
            
    print(answer)
    return

#tests
valid_palidrome_with_removal('abcba') # ->> true
valid_palidrome_with_removal('foobof') # ->> true
valid_palidrome_with_removal('abccab') # ->> false
