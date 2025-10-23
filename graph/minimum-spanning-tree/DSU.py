# dus -> (Not recommended using python, but it works)


# IDEA: Fast input/output
import sys

input = lambda: sys.stdin.buffer.readline().decode().rstrip()

# IDEA: Simple to write Fast input/output
II = lambda: int(input())
MII = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())

class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)
    
    def find(self, x):
        # Iterative path compression to avoid recursion depth issues
        root = x
        while self.parent[root] != root:
            root = self.parent[root]

        # compress path
        while self.parent[x] != x:
            parent = self.parent[x]
            self.parent[x] = root
            x = parent

        return root
    
    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False  # Already connected
        # Union by size
        if self.size[rx] < self.size[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        self.size[rx] += self.size[ry]
        return True
    
    def connected(self, x, y):
        return self.find(x) == self.find(y)

# Example usage:
n, m = MII()
dsu = DSU(n)

for _ in range(m):
    u, v = MII()
    dsu.union(u, v)

q = II()
for _ in range(q):
    a, b = MII()
    # is a and b connected?
    if dsu.connected(a, b):
        print("YES")
    else:
        print("NO")