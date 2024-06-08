# This question is asked by Amazon. Given a 2D matrix that represents a gold mine, where each cell’s value represents an amount of gold, return the maximum amount of gold you can collect given the following rules:

# You may start and stop collecting gold from any position
# You can never visit a cell that contains 0 gold
# You cannot visit the same cell more than once
# From the current cell, you may walk one cell to the left, right, up, or down
# Ex: Given the following gold mine…

# goldMine = [
#     [0,2,0],
#     [8,6,3],
#     [0,9,0]
# ],
# return 23 (start at 9 and then move to 6 and 8 respectively)

goldMine = [
    [0,2,0],
    [8,6,3],
    [0,9,0]
]

def maxx(i, j, visited:set = set()):
    if((i,j) in visited):
        return 0
    
    if i < 0 or j < 0 or i > len(goldMine) - 1 or j > len(goldMine[i]) -1:
        return 0
    
    if(goldMine[i][j] == 0):
        return 0

    visited.add((i,j))
    
    left = maxx(i, j-1, visited)
    right = maxx(i, j+1, visited)
    up = maxx(i-1, j, visited)
    down = maxx(i+1, j, visited)
    
    
    return goldMine[i][j] + max(left, right, up, down)
    
def max_gold():
    answers = []
    
    for i in range(len(goldMine)):
        for j in range(len(goldMine[i])):
            answers.append(maxx(i, j, visited=set()))
    
    print(max(answers))
            

max_gold()