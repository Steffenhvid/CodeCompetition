import numpy as np

def is_number_increasing(number):
    numberstring = str(number)
    for i in range(len(numberstring) - 1):
        if numberstring[i] > numberstring[i+1]:
            return False
        
    return True

def is_number_decreasing(number):
    numberstring = str(number)
    for i in range(len(numberstring) - 1):
        if numberstring[i] < numberstring[i+1]:
            return False
        
    return True

def is_number_bouncy(number):
    return not is_number_increasing(number) and not is_number_decreasing(number)

ratio = 0.0
number_of_bouncies = 0
i = 0
while ratio != 99:
    i += 1
    if is_number_bouncy(i):
        number_of_bouncies += 1
        ratio = np.round(np.floor((number_of_bouncies/i)*100))
    

print(i)