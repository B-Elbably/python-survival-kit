"""
    3-color method (white/gray/black) 
                    (0  / 1  / 2)
"""


# IDEA: Fast input/output
import sys
input = lambda: sys.stdin.buffer.readline().decode().rstrip()

# IDEA: Modules
from collections import defaultdict

# IDEA: Simple to write Fast input/output
II = lambda: int(input())
MII = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())

def is_cycle_directed(n, adj):
    color = [0] * (n + 1)  # 0=unvisited, 1=visiting, 2=visited
    
    def dfs(u):
        color[u] = 1  # Visiting
        for v in adj[u]:
            if color[v] == 0:  # Unvisited
                if dfs(v):
                    return True
            elif color[v] == 1:  # Back edge
                return True
        color[u] = 2  # Visited
        return False
    
    for i in range(1, n + 1):
        if color[i] == 0:
            if dfs(i):
                return True
    return False

n, m = MII()
adj = defaultdict(list)
for _ in range(m):
    u, v = MII()
    adj[u].append(v)

if is_cycle_directed(n, adj):
    print("Cycle exists")
else:
    print("No cycle")

