# This question is asked by Facebook. Given two strings s and t return whether or not s is an anagram of t.
# Note: An anagram is a word formed by reordering the letters of another word.

# Ex: Given the following strings...

# s = "cat", t = "tac", return true
# s = "listen", t = "silent", return true
# s = "program", t = "function", return false

def is_valid_anagram(s : str, t: str):
    s_sort = ''.join(sorted([*s]))
    t_sort = ''.join(sorted([*t]))

    print(sorted(s) == sorted(t))

#tests
is_valid_anagram('cat', 'tac')
is_valid_anagram('listen', 'silent')
is_valid_anagram('program', 'function')