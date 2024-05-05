import math
import time


def triangle(n):
    return int((n*(n+1))/2)

def pentangle(n):
    return int((n*(3*n-1))/2)

def hexangle(n):
    return n * (2*n - 1)

start_time = time.time()

x = 285
y = 165
z = 143

def test(n):
    return (1/6) * (math.sqrt(48*n*n-24*n+1)+1)

conti = True

while conti:
    z += 1
    candidate = test(z)
    if (candidate % 1 == 0):
        conti = False

print(candidate)
print(pentangle(candidate))
end_time = time.time()
print(end_time-start_time)

