# This question is asked by Google. Given a string s, return all possible partitions of s such that each substring is a palindrome.

# Ex: Given the following string s…

# s = "abcba",
# return [
#     ["a","b","c","b","a"],
#     ["a","bcb","a"],
#     ["abcba"]
# ]

def isPalindrome(s: str) -> bool:
        l = 0
        r = len(s) - 1
        
        while l < r:
            if s[l] != s[r]:
                return False
            l = l + 1
            r = r - 1
            
        return True

def palindromic_partitions(s: str):
    answer = []    
    
    def recurse(s:str, output = []):
        if len(s) == 0:
            answer.append(output.copy())
            return
            
        
        for i in range(len(s)):
            take = s[: i+1 ] # take the first ith subset of the string
            remainder = s[i + 1: ]
            
            output.append(take)
            
            if isPalindrome(take):
                recurse(remainder, output)
            output.pop()
        pass
    
    recurse(s)
    print(answer)

palindromic_partitions('abcba')