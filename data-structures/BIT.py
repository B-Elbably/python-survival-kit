# BIT -> Binary Indexed Tree == Fenwick Tree

class BIT:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def update(self, i, delta):
        while i <= self.n:
            self.bit[i] += delta
            i += i & -i

    def query(self, i):
        s = 0 # skip value 
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

    def range_query(self, l, r):
        return self.query(r) - self.query(l - 1)


"""
    skip value:
    sum -> 0
    min -> inf
    max -> -inf
    multiply -> 1
    gcd -> 0
    xor -> 0
    and -> -1
    or -> 0
"""