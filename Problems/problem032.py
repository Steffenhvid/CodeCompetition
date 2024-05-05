import time
import sys
sys.path.append(".\\")
import Services.Numbers.Pandigital as s

sum = 0
for i in range(1,10000):
    if s.PandigitalProduct_1_9(i):
        print(i)
        sum += i

print(sum)


