# This question is asked by Microsoft. Given a string, return the index of its first unique character. If a unique character does not exist, return -1.

# Ex: Given the following strings...

# "abcabd", return 2
# "thedailybyte", return 1
# "developer", return 0


def first_unique_character(s: str):
    map = dict()
    lst = s.split()
    
    for i in s:
        if i in map:
            map[i] += 1
        else:
            map[i] = 1
            
    for i in s:
        if map[i] == 1:
            print(s.index(i))
            return
            

#tests
first_unique_character('abcabd')
first_unique_character('thedailybyte')
first_unique_character('developer')