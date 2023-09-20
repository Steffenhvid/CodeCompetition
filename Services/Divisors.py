import math

#does not work!
def divisors(n):
    divisors = [1]
    sqrt_n = int(math.sqrt(n))
    for i in range(2, sqrt_n + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    if sqrt_n * sqrt_n == n:
        divisors.remove(sqrt_n)
    return divisors

divisorSums = dict()
for i in (1,10001):
    print(sum(divisors(i)))
