def isCircular(a : str) -> str:
    path = [0,0]

    for i in a:
        if i == 'L':
            path[0] = path[0] - 1
        if i == 'R':
            path[0] = path[0] + 1
        if i == 'U':
            path[1] = path[1] + 1
        if i == 'D':
            path[1] = path[1] - 1
    
    print(path == [0,0])


isCircular('LR')
isCircular('URURD')
isCircular('RUULLDRD')