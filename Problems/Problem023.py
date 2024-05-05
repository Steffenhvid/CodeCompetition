from itertools import combinations
import sys
sys.path.append(".\\")
print(sys.path)

from Services.Divisors import Divisors

p42 = Divisors()

abundentNums = []

for i in range(1, 28124):
    divisor = p42.get_proper_divisors_off(i)
    s = sum(divisor)
    isAbundant = i < s
    #print(str(i) + ":" + str(divisor) + " => " + str(s) +","+ str(isAbundant))
    if isAbundant:
        abundentNums.append(i)

sums = [0]*28124
for x in range (0, len(abundentNums)):
    for y in range (x, len(abundentNums)):
            sumOf2AbundantNums = abundentNums[x]+abundentNums[y]
            if (sumOf2AbundantNums<= 28123):
                if (sums[sumOf2AbundantNums] == 0):
                    sums[sumOf2AbundantNums] = sumOf2AbundantNums

total = 0
for x in range (1,len(sums)):
    if (sums[x] == 0):
        total +=x

print(total)