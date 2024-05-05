import math

def cc(a,b):
    return math.sqrt(a*a+b*b)

def bb(a,p):
    return (p*(a-p/2))/(a-p)

results = {}

for p in range(1, 1001):
    results[p] = 0
    for a in range(1, math.ceil(p/2)):
        b = bb(a,p)
        if b % 1 == 0:
            c = cc(a,b)
            if c % 1 == 0:
                results[p] += 1

print(max(results, key=results.get))