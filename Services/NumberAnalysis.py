

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