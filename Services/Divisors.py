import math
from itertools import combinations

class Divisors:
    def __init__(self):
        pass

    def get_proper_divisors_off(self, number:int) -> list[int]:
        '''
        Returns a list of prober divisors
        i.e. 12 -> [1,2,3,4,6]
        '''
        divisors = [1]
        for i in range(2, math.ceil(math.sqrt(number))):
            if(number % i == 0):
                divisors.append(i)
                divisors.append(int(number/i))
        return divisors
    
    def is_abundant(self, number:int) -> bool:
        return sum(self.get_proper_divisors_off(number)) > number
    
    def get_all_abundant_in_range(self, upperlimit:int) -> dict[int, bool]:
        numbers = {i: self.is_abundant(i) for i in range(1,upperlimit)}
        return [k for k in numbers.keys() if numbers[k]]

test = Divisors()
test1 = test.get_all_abundant_in_range(28124)
test2 = set([sum(i) for i in map(sorted, combinations(set(test1), 2))])
test3 = set(range(28124))
print(sum(test3.difference(test2)))
