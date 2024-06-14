# This question is asked by Amazon. You’re running a popsicle stand where each popsicle costs $5. Each customer you encountered pays with either a $5 bill, a $10 bill, or a $20 bill and only buys a single popsicle. the customers that come to your stand come in the ordered given by the customers array where customers[i] represents the bill the ith customer pays with. Starting with $0, return whether or not you can serve all the given customers while also giving the correct amount of change.

# Ex: Given the following customers…

# customers = [5, 10], return true
# collect $5 from the first customer, pay no change.
# collet $10 from the second customer and give back $5 change.

# Ex: Given the following customers…

# customers = [10], return false
# collect $10 from the first customer and we cannot give back change.

# Ex: Given the following customers…

# customers = [5,5,5,10,20], return true
# collect $5 from the first 3 customers.
# collet $10 from the fourth customer and give back $5 change.
# collect $20 from the fifth customer and give back $10 change ($10 bill and $5 bill).



# I will check whether I have change <- bill - price

def can_serve(bills):
    five = ten = 0
    for i in bills:
        if i == 5: five += 1
        elif i == 10:
            if five == 0:
                print(False)
                return
            else:
                five -= 1
                ten += 1
        elif i == 20:
            if ten > 0 and five > 0:
                ten = ten -1
                five = five - 1
            else:
                five = five - 3
                if five < 0:
                    print(False)
                    return
    
    print(True)
        
can_serve([5,10]) # true
can_serve([10]) # false
can_serve([5,5,5, 10,20]) # true