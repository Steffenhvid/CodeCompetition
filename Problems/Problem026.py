import sys
from typing import List
sys.path.append(".\\")

primes = [7, 11, 13, 17, 19, 23, 29,
  31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
  73, 79, 83, 89, 97, 101, 103, 107, 109, 113,
  127, 131, 137, 139, 149, 151, 157, 163, 167, 173,
  179, 181, 191, 193, 197, 199, 211, 223, 227, 229,
  233, 239, 241, 251, 257, 263, 269, 271, 277, 281,
  283, 293, 307, 311, 313, 317, 331, 337, 347, 349,
  353, 359, 367, 373, 379, 383, 389, 397, 401, 409,
  419, 421, 431, 433, 439, 443, 449, 457, 461, 463,
  467, 479, 487, 491, 499, 503, 509, 521, 523, 541,
  547, 557, 563, 569, 571, 577, 587, 593, 599, 601,
  607, 613, 617, 619, 631, 641, 643, 647, 653, 659,
  661, 673, 677, 683, 691, 701, 709, 719, 727, 733,
  739, 743, 751, 757, 761, 769, 773, 787, 797, 809,
  811, 821, 823, 827, 829, 839, 853, 857, 859, 863,
  877, 881, 883, 887, 907, 911, 919, 929, 937, 941,
  947, 953, 967, 971, 977, 983, 991, 997]

def get_long_division_cycle_length(denominator: int) -> int:
    numerator = 10
    digits = []
    remainders = []
    cur = numerator
    while True:
        digit = cur // denominator
        cur = cur % denominator
        if cur in remainders:
            break
        digits.append(digit)
        remainders.append(cur)
        cur *= 10
        if cur == 0:
            return 0
        while cur < denominator:
            cur *= 10
            digits.append(0)
    while remainders[0] != cur:
        remainders.pop(0)
    return len(remainders)

def solution_long_division(numbers:List[int]) -> int:
    cycle_lengths = {denominator: get_long_division_cycle_length(denominator) for denominator in numbers}
    return sorted(cycle_lengths.items(), key=lambda item: item[1])[-1][0]
   
print(solution_long_division(primes))