# This question is asked by Google. You are given a bag of coins, an initial energy of E, and want to maximize your number of points (which starts at zero). To gain a single point you can exchange coins[i] amount of energy (i.e. if I have 100 energy and a coin that has a value 50 I can exchange 50 energy to gain a point). If you do not have enough energy you can give away a point in exchange for an increase in energy by coins[i] amount (i.e. you give away a point and your energy is increased by the value of that coin: energy += coins[i]). Return the maximum number of points you can gain.
# Note: Each coin may only be used once.

# Ex: Given the following coins and starting energy…

# coins = [100, 150, 200] and E = 150, return 1
# coins = [100,200,300,400] and E = 200, return 2
# coins = [300] and E = 200, return 0


# def max_points(coins: list, E: int):
#     # base case
#     # if len(coins) == 0
#     # if E < coins[0] and points == 0
    
#     globals = {
#     'point': 0
#     }

#     def recurse(coins: list, E: int, points=0):
#         globals['point'] = max(globals['point'], points)
        
#         if len(coins) == 0:
#             return

#         if E < coins[0] and points == 0:
#             return


#         for i in range(len(coins)):
#             remainder = coins[0: i] + coins[i+1:]
#             last = coins[-1]

#             for j in range(2):
#                 if E >= coins[i]:
#                     recurse(remainder, E - coins[i], points+1)

#                 if points > 0:
#                     recurse(coins[:-1] , E + last, points - 1)


#     recurse(coins, E)
#     print(globals['point'])

def max_points(coins: list, E: int):
    l = 0
    r = len(coins) - 1
    max_points = 0
    points = 0
    
    while l <= r:
        if E >= coins[l]:
            # Gain a point
            E -= coins[l]
            points += 1
            max_points = max(max_points, points)
            l += 1
        elif points > 0:
            # Trade a point for energy
            E += coins[r]
            points -= 1
            r -= 1
        else:
            break

    print(max_points)

max_points([100, 150, 200], 150)
max_points([100, 200, 300, 400 ], 200)
max_points([300], 200)