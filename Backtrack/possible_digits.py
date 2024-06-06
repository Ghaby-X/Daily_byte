# This question is asked by Google. Given a string of digits, return all possible text messages those digits could send. Note: The mapping of digits to letters is as follows…

# 0 -> null
# 1 -> null
# 2 -> "abc"
# 3 -> "def"
# 4 -> "ghi"
# 5 -> "jkl"
# 6 -> "mno"
# 7 -> "pqrs"
# 8 -> "tuv"
# 9 -> "wxyz"
# Ex: digits = "23" return ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

def possible_digits(sequence: str):
    digit_map = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
    }
    
    result = []
    depth = len(sequence)
    
    def backtrack(sequence: str, idx, output: list):
        if idx == depth:
            result.append("".join(output))
            return
        
        digit_array = digit_map[sequence[idx]]
        
        for i in digit_array:
            output.append(i)
            backtrack(sequence, idx + 1, output)
            output.pop()
        
    backtrack(sequence, 0, [])
    print(result)
    pass

possible_digits('23')
possible_digits('2')
possible_digits('')