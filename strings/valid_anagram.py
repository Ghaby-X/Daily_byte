# This question is asked by Facebook. Given two strings s and t return whether or not s is an anagram of t.
# Note: An anagram is a word formed by reordering the letters of another word.

# Ex: Given the following strings...

# s = "cat", t = "tac", return true
# s = "listen", t = "silent", return true
# s = "program", t = "function", return false


# def is_valid_anagram(s : str, t: str):
#     s_sort = ''.join(sorted([*s]))
#     t_sort = ''.join(sorted([*t]))

#     print(sorted(s) == sorted(t))


def is_valid_anagram(s:str, t: str):
    map = dict()
    
    for i in s:
        if i in map:
            map[i] =map[i] + 1
        else:
            map[i] = 1
    
    for i in t:
        if i in map:
            map[i] -= 1
        else:
            print(False)
            return
    
    for i in map.keys():
        if map[i] != 0:
            print(False)
            return
    
    print(True)


#tests
is_valid_anagram('cat', 'tac')
is_valid_anagram('listen', 'silent')
is_valid_anagram('program', 'function')