import math

def FactorialDigitSum():
    fact = dict()
    fact[0] = 1

    for i in range(1,10):
        fact[i] = i * fact[i-1]

    factSum = dict()

    for j in range(1,100000):
        stringJ = str(j)
        subStringJ = stringJ[:-1]
        lastDigit = int(stringJ[-1])
        if len(subStringJ) > 0:
            intSubString = int(subStringJ)
            if intSubString in factSum.keys():
                factSum[j] = factSum[intSubString] + fact[lastDigit]
        else:
            factSum[j] = fact[j]
        if factSum[j] ==j:
            print(j)