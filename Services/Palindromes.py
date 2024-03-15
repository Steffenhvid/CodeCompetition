import math

def createPalindrome(inp, b, isOdd): 
    n = inp 
    palin = inp 
   
    # checks if number of digits is odd or even 
    # if odd then neglect the last digit of input in 
    # finding reverse as in case of odd number of 
    # digits middle element occur once 
    if (isOdd): 
        n = n // b 
   
    # Creates palindrome by just appending reverse 
    # of number to itself 
    while (n > 0): 
        palin = palin * b + (n % b) 
        n = n // b 
    return palin 
   
# Function to print decimal palindromic number 
def generatePalindromes(n) -> list[int]: 
    result = []
    # Run two times for odd and even length palindromes 
    for j in range(2): 
        # Creates palindrome numbers with first half as i.  
        # Value of j decided whether we need an odd length 
        # of even length palindrome. 
        i = 1
        while (createPalindrome(i, 10, j % 2) < n):
            result.append(createPalindrome(i, 10, j % 2))
            i = i + 1
    return result

def isPalindrome(word:str) -> bool:
    reversed = list(word)
    reversed.reverse()
    reversed = "".join(reversed)
    return word == reversed

def count_pal(n):
    '''counts all palindromes to the nth power 10^n'''
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