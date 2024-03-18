#This question is asked by Microsoft. Given an array of strings, return the longest common prefix that is shared amongst all strings.
#Note: you may assume all strings only contain lowercase alphabetical characters.

# Ex: Given the following arrays...

# ["colorado", "color", "cold"], return "col"
# ["a", "b", "c"], return ""
# ["spot", "spotty", "spotted"], return "spot"

def longest_common_prefix(arr):
    substring = []
    short = min(arr)

    for i in range(len(short)):
        inpresent = True

        for j in arr:
            if j[i] != short[i]:
                inpresent = False
                break
        
        if inpresent:
            substring.append(short[i])
        else:
            break
    print(''.join(substring)) 


longest_common_prefix(["colorado", "color", "cold"])
longest_common_prefix(["a", "b", "c"])
longest_common_prefix(["spot", "spotty", "spotted"])
