import sys
sys.path.append(".\\")
import Services.Primes as p

primeCandidates = p.primes_sieve_of_eratosthenes(99999999)
for p in primeCandidates:
    strp = str(p)
    setp = set(strp)
    n = len(strp)
    s = set()
    for i in range(1,n+1):
        s.add(str(i))
    if s == setp:
        print(p)


