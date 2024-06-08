# This question is asked by Amazon. Given a 2D board that represents a word search puzzle and a string word, return whether or the given word can be formed in the puzzle by only connecting cells horizontally and vertically.

# Ex: Given the following board and words…

# board =
# [
#   ['C','A','T','F'],
#   ['B','G','E','S'],
#   ['I','T','A','E']
# ]
# word = "CAT", return true
# word = "TEA", return true
# word = "SEAT", return true
# word = "BAT", return false

board = [
  ['C','A','T','F'],
  ['B','G','E','S'],
  ['I','T','A','E']
]

board_length = len(board)

def check(loc: tuple, word: str) -> bool:
    current_val = board[loc[0]][loc[1]]
    
    # check if value at location is equal to first word of string
    if (current_val != word[0]):
        return False
    
    # check boundaries
    if (loc[0] > len(board) - 1 or loc[1] > len(board[loc[0]]) -1 or loc[0] < 0 or loc[1] < 0):
        return False
    
    # check if last word has been reached
    if len(word) == 1 and current_val == word[0]:
        return True
    
    # generate left and right codes
    left = (loc[0], loc[1] - 1)
    right = (loc[0], loc[1] + 1)
    up = (loc[0] - 1, loc[1])
    down = (loc[0] + 1, loc[1])
    
    if check(left, word[1:]) or check(right, word[1:]) or check(up, word[1:]) or check(down, word[1:]):
        return True
    
    return False

def board_search(word: str):
    answer = False
    
    for i in range(len(board)):
        for j in range(len(board[i])):
            answer = answer or check((i,j),word)
        
    print(answer)
    pass

board_search('CAT')
board_search('TEA')
board_search('SEAT')
board_search('BAT')