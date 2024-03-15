'''
Rectangle packing problem
'''

class rectangle():
    def __init__(self, x:int, y:int):
        self.height = max(x,y)
        self.width = min(x,y)
        self.area = x*y

    def __str__(self):
        return f"{self.height}x{self.width}={self.area}"

def packing_rectangles(a1, b1, a2, b2, a3, b3):
    A = rectangle(a1,b1)
    B = rectangle(a2,b2)
    C = rectangle(a3,b3)

    rectangles = [A, B, C]
    rectangles.sort(key=lambda x:x.height, reverse=True)
    for rec in rectangles:
        print(rec)

for i in range(20):
    print(i * i)

from itertools import permutations

def number_filter(a,upperlimit):
    number = int(''.join(map(str, a)))
    return number <= upperlimit

def max_filter(a):
    return int(''.join(map(str, a)))

def latest_clock(a, b, c, d):
    data = [a,b,c,d]
    permuts = permutations(data,2)

    possiple_hours = list(filter(lambda n:number_filter(n,23), permuts))
    possiple_hours.sort(key=max_filter, reverse=True)

    for hour in possiple_hours:
        remaining_digits = [i for i in data]
        remaining_digits.remove(hour[0])
        remaining_digits.remove(hour[1])
        possible_minuttes = list(filter(lambda n: number_filter(n,59), permutations(remaining_digits)))
        possible_minuttes.sort(key=max_filter, reverse=True)
        if(len(possible_minuttes) > 0):
            max_minutes = possible_minuttes[0]
            return f"{hour[0]}{hour[1]}:{max_minutes[0]}{max_minutes[1]}"

    return "00:00"
    

print(latest_clock(1,2,8,9))
    
from itertools import *

late_clock = lambda *a: max("%s%s:%s%s" % c for c in permutations(a) if c[:2] < (2, 4) and c[2] < 6)