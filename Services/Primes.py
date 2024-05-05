from itertools import permutations
import math

def primes_sieve_of_eratosthenes(n:int) -> list[int]:
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
 
        # If prime[p] is not
        # changed, then it is a prime
        if (prime[p]):
 
            # Update all multiples of p
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    primes = []
    # Print all prime numbers
    for p in range(2, n+1):
        if prime[p]:
            primes.append(p)
    return primes

def all_sieve_of_eratosthenes(limit:int) -> dict:
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False  

    for p in range(2, int(limit**0.5) + 1):
        if is_prime[p]:            
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False

    primes = {index: element for index, element in enumerate(is_prime)}
    return primes

def create_combination_of_number(number:int) -> list[int]:
    number_string = str(number)
    digit_permutations = set(permutations(number_string))
    return [int(''.join(permutation)) for permutation in digit_permutations]

# Does not work currently
def find_circular_primes(limit:int) -> int:
    primes = primes_sieve_of_eratosthenes(limit)
    i = 0
    for p in primes:
        if not any(char in '02468' for char in str(p)) or p == 2:
            permutation = set(create_combination_of_number(p))
            if(permutation.issubset(primes)):
                print(str(p) + ': ' + str(permutation))
                i += 1
    return i

def is_prime(x:int) -> bool:
    if(x <= 1):
        return False
    if x in [2]:
        return True
    for i in range(3,math.floor(math.sqrt(x))+1):
        if x % i == 0:
            return False
        
    return True




