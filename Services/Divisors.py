import math

class Divisors:
    def __init__(self):
        pass

    def get_proper_divisors_off(self, number:int) -> list[int]:
        '''
        Returns a list of prober divisors
        i.e. 12 -> [1,2,3,4,6]
        '''
        divisors = [1]
        for i in range(2, math.floor(math.sqrt(number))+1):
            if(number % i == 0):
                divisors.append(i)
                divisors.append(int(number/i))
        return list(set(divisors))
    
    def is_abundant(self, number:int) -> bool:
        return sum(self.get_proper_divisors_off(number)) > number
    
    def get_all_abundant_in_range(self, upperlimit:int) -> dict[int, bool]:
        numbers = {i: self.is_abundant(i) for i in range(1,upperlimit)}
        return [k for k in numbers.keys() if numbers[k]]
