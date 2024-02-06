import sys
sys.path.append(".\\")
import Services.Primes as p

def uniquePairs(arr):
    # Set to store unique pairs
    s = set()
    n = len(arr)
 
    # Make all possible pairs
    for i in range(n):
        for j in range(n):
            s.add(int(str(arr[i]) + str(arr[j])))
 
    # Return the size of the set
    return list(s)
 
def test(n):
    res = []
    even = set(["0","2","4","6","8"])
    for i in range(n):
        if(i > 99):
            number = set(str(i))
        else:
            number = str(i)

        if len(even.intersection(number)) == 0:
            res.append(i)
    return set(res)

final = test(1000000)

# for some reason it does not find 23 as a valid number.
for i in final:
    k1 = i
    k2 = i
    while p.is_prime(k1) :
        s1 = list(str(k1))
        s1.pop(0)
        if(len(s1) > 0 ):
            k1 = int("".join(s1))
        else:
            k1 = 0
    if k1 == 0:
        while p.is_prime(k2):
            s2 = list(str(k2))
            s2.pop(-1)
            if(len(s2) > 0 ):
                k2 = int("".join(s2))
            else:
                k2 = 0
    if k1 == 0 and k2 == 0:
        print(i)

# Stolen solution
def problem37():
    
    n, m = (1000000 - 1)/2, int((1000000 ** 0.5)//1 - 1)/2
    n = int(n)
    m = int(m)
    a, e, z = [True] * n, ['2', '0', '4', '6', '8'], 23
    for i in range(m):
        if a[i]:
            s = i + i + 3
            t = (s ** 2)/2 - 1
            t = int(t)
            for j in range(t, n, s):
               a[j] = False
    for x in range(10, n):
        if a[x]:
            p, b = 2 * x + 3, True
            for d in str(p)[1:]:
                if d in e:
                    b = False
                    break
            if b and str(p)[0] in e[2:] or str(p)[0] == '1' or str(p)[-1] == '1': b = False
            if b:
                for i in range(1, len(str(p))):
                    q = (int(str(p)[i:]) - 3)/2
                    q = int(q)
                    r = (int(str(p)[:i]) - 3)/2
                    r = int(r)
                    if not a[q] or not a[r]:
                        b = False
                        break
                if b: 
                    z += p
                    print(p)
    return z

