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
 
def uniqueTripelets(arr):
    # Set to store unique pairs
    s = set()
    n = len(arr)
 
    # Make all possible pairs
    for i in range(n):
        for j in range(n):
            for k in range(n):
                s.add(int(str(arr[i]) + str(arr[j]) + str(arr[k])))
 
    # Return the size of the set
    return [i for i in s]
 
# Driver code
 
arr = [1, 3, 5, 7, 9]
arr = arr + uniquePairs(arr)
arr = arr + uniquePairs(arr)
arr = arr + uniquePairs(arr)

for i in arr:
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

