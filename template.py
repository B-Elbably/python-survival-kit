# لا تَجلِس فارِغًا [ حرك لسانك ]
# اسْتَغفِر ، سَبّح ، هَلّل ، كَبّر ، حَولق

import sys
from random import randint, shuffle, choice
from math import gcd, sqrt, isqrt, perm, log, comb, factorial, log2, ceil, floor
from collections import Counter, defaultdict, deque
from functools import lru_cache, reduce, cmp_to_key
from itertools import (
    accumulate,
    combinations,
    permutations,
    product,
    repeat,
    takewhile,
    starmap,
    dropwhile,
    cycle,
)
from heapq import (
    nsmallest,
    nlargest,
    heappushpop,
    heapify,
    heappop,
    heappush,
    _heapify_max,
)
from bisect import bisect_left, bisect_right, insort_left, insort_right

# from operator import sub, mul, pow, truediv, floordiv
input = lambda: sys.stdin.buffer.readline().decode().rstrip()
OneByOne = lambda: sys.stdin.read(1)


def lcm(a, b):
    return a * b // gcd(a, b)


def W(i):
    return (i, str(i))


def MakeFile(s: str, r="in", v="out"):
    import sys

    sys.stdin = open(f"{s}.{r}", "r")
    sys.stdout = open(f"{r}.{v}", "w")


I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LGMI = lambda: list(map(lambda x: int(x) - 1, input().split()))
yes = lambda: print("YES")
no = lambda: print("NO")
letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]
DIR4 = ((-1, 0), (0, 1), (1, 0), (0, -1))
DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))
DIR4_prime = [(-1, 0, "U"), (0, 1, "R"), (1, 0, "D"), (0, -1, "L")]
MOD = 10**9 + 7
inf = float("inf")

# for _ in range(II()):
