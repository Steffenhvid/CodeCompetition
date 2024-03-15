import math
from itertools import product

def count_pal(n):
    accounting = {}
    if n > 0:
        accounting[1] = [9, 9]
    # if n > 1:
    #     accounting[2] = [9, 9 + accounting[1][1]]
    # if n > 2:
    for i in range(2,n+1):
        alpha = math.floor(i/2)
        if i % 2 == 0:
            amount = int("1"+"0" * (alpha-1)) * 9
            accounting[i] = [amount, amount + accounting[i-1][1]] 
        else:
            amount = int("1"+"0"*alpha) * 9
            accounting[i] = [amount, amount + accounting[i-1][1]]
    
    return accounting.get(n, None)

print(count_pal(3))