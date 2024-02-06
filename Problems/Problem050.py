import sys
sys.path.append(".\\")

from Services.Primes import primes_sieve_of_eratosthenes, is_prime

test = primes_sieve_of_eratosthenes(1000000)
candidates = []
i = 0
while sum(candidates) + test[i] <= 1000000:
    candidates.append(test[i])
    i +=1

j = len(candidates)
total = sum(candidates)
while not is_prime(total):
    candidates.pop(0)
    total = sum(candidates)

print(candidates)
print(len(candidates))
print(sum(candidates))