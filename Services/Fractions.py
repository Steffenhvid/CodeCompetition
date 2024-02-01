from math import gcd 
 
# Function to reduce a fraction 
# to its lowest form
def reduceFraction(x, y) :
     
    d = gcd(x, y)
 
    x = x // d
    y = y // d
 
    return [x,y]