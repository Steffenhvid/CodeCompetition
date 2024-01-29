def is_pandigital(n:str) -> bool:
    if len(n) != 9:
        return False
    
    n = "".join(sorted(n))
    return n == "123456789"

def PandigitalProduct_1_9(n): 
     
    i = 1
    while i * i <= n:
         
        if ((n % i == 0) and
             bool(is_pandigital(str(n) +
                               str(i) +
                               str(n // i)))):
            return bool(True)
             
        i += 1
     
    return bool(False)
