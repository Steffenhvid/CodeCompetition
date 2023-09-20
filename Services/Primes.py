from itertools import permutations

def primes_sieve_of_eratosthenes(limit:int) -> list[int]:
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False  

    for p in range(2, int(limit**0.5) + 1):
        if is_prime[p]:            
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False

    primes = [p for p in range(2, limit + 1) if is_prime[p]]
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


