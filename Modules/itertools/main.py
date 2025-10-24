# 1- Permutations -> O(n! / (n-r)!)
print(" <==== Permutations ===>")
from itertools import permutations

numbers = [1, 2, 3]
for perm in permutations(numbers):  # all orderings of elements
    print(perm)  # tuple


# 2- Combinations -> O(n! / (r!(n-r)!))
print("\n <==== Combinations ===>")
from itertools import combinations

numbers = [1, 2, 3, 4]
for c in combinations(numbers, 2):  # all r-length subsets
    print(c)  # tuple

"""
combinations_with_replacement: allows repeated elements
T.C: O(C(n+r-1, r)), S.C: O(r)
"""


# 3- Cartesian Products -> O(n^r)
print("\n <==== Cartesian Products ===>")
from itertools import product

for p in product([0, 1], repeat=3):  # all r-length tuples
    print(p)


# 4- Accumulate -> cumulative sums (or other binary functions)
print("\n <==== Accumulate ===>")
from itertools import accumulate

numbers = [2, 3, 4, 7, 2]
print(list(accumulate(numbers)))  # prefix sum

"""
Default is sum.
T.C: O(n), S.C: O(n)
Use func for other ops, e.g., operator.mul
"""


# 5- GroupBy -> group consecutive identical elements
print("\n <==== GroupBy ===>")
from itertools import groupby

data = [1, 1, 2, 2, 3, 1, 1]
for k, g in groupby(data):
    print(k, list(g))


# 6- Cycle -> infinite iterator
print("\n <==== Cycle ===>")
from itertools import cycle

count = 0
for x in cycle([1, 2, 3]):
    print(x, end=' ')
    count += 1
    if count == 10:  # stop manually
        break


# 7- islice -> slice without creating a list
print("\n <==== islice ===>")
from itertools import islice

nums = range(10)
print(list(islice(nums, 2, 8, 2)))  # start:stop:step
