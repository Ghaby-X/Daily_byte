# This question is asked by Apple. You are serving people in a lunch line and need to ensure each person gets a “balanced” meal. A balanced meal is a meal where there exists the same number of food items as drink items. Someone is helping you prepare the meals and hands you food items (i.e. F) or a drink items (D) in the order specified by the items string. Return the maximum number of balanced meals you are able to create without being able to modify items.
# Note: items will only contain F and D characters.

# Ex: Given the following items…

# items = "FDFDFD", return 3
# the first "FD" creates the first balanced meal.
# the second "FD" creates the second balanced meal.
# the third "FD" creates the third balanced meal.
# Ex: Given the following items…

# items = "FDFFDFDD", return 2
# "FD" creates the first balanced meal.
# "FFDFDD" creates the second balanced meal.

def balanced_meals(items: str):
    total = 0
    F = 0
    D = 0
    
    for i in items:
        if i == "F":
            F += 1
        else:
            D += 1
            
        if F == D and F > 0 and D > 0:
            F = 0
            D = 0
            total += 1

    print(total)

balanced_meals("FDFDFD")
balanced_meals("FDFFDFDD")