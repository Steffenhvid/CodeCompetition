import math
import sys
sys.path.append(".\\")

from Services.Primes import is_prime

def quadraticFunction(a:int, b:int, n:int) -> int:
    return(int(math.pow(n,2) + a*n + b))


longestRun = 0
result = [-1001, -1001]
for i in range(-999,1000):
    for j in range(-1000,1001):
        cont = True
        n = 0
        run = 0
        while(cont):
            value = quadraticFunction(i,j,n)
            if(is_prime(value)):
                n += 1
                run += 1
            else:
                if(longestRun < run):
                    longestRun = run
                    result[0] = i
                    result[1] = j
                cont = False

print(longestRun)
print(result[0])
print(result[1])
print(result[0]*result[1])
