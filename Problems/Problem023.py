from itertools import combinations
import sys
sys.path.append(r".\\")

from Services.Divisors import Divisors

test = Divisors()
test1 = test.get_all_abundant_in_range(28124)
test2 = set([sum(i) for i in map(sorted, combinations(set(test1), 2))])
missing_sums = set([i+i for i in test1])
abondant_sums = test2.union(missing_sums)
all_numbers = set(range(28124))
print(sum(all_numbers.difference(abondant_sums)))