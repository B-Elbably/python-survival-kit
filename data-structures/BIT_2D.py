class BIT2D:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.bit = [[0] * (m + 1) for _ in range(n + 1)]

    def add(self, x, y, val):
        """Add `val` to element at (x, y)."""
        i = x + 1
        while i <= self.n:
            j = y + 1
            while j <= self.m:
                self.bit[i][j] += val
                j += j & -j
            i += i & -i

    def sum(self, x, y):
        """Compute the prefix sum from (0,0) to (x,y) inclusive."""
        res = 0
        i = x + 1
        while i > 0:
            j = y + 1
            while j > 0:
                res += self.bit[i][j]
                j -= j & -j
            i -= i & -i
        return res

    def range_sum(self, x1, y1, x2, y2):
        """Compute the sum of the rectangle defined by (x1,y1) and (x2,y2) inclusive."""
        return (self.sum(x2, y2)
                - self.sum(x1 - 1, y2)
                - self.sum(x2, y1 - 1)
                + self.sum(x1 - 1, y1 - 1))
        
    def range_sum(self, x1 , y1) :
        return self.range_sum(0, 0, x1, y1)