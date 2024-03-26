# This question is asked by Amazon. Given a string representing your stones and another string representing a list of jewels, return the number of stones that you have that are also jewels.

# Ex: Given the following jewels and stones...

# jewels = "abc", stones = "ac", return 2
# jewels = "Af", stones = "AaaddfFf", return 3
# jewels = "AYOPD", stones = "ayopd", return 0

def common_items(j: str, s: str):
    j_set = set(j)
    print(sum(i in j_set for i in s))
    return

#tests
common_items('abc', 'ac') # ->> 2
common_items('Af', 'AaaddfFf') # ->> 3
common_items('AYOPD', 'ayopd') # ->> 0
