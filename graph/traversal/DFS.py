# IDEA: Fast input/output
import sys

input = lambda: sys.stdin.buffer.readline().decode().rstrip()

# IDEA: Modules
from collections import defaultdict

# IDEA: Simple to write Fast input/output
II = lambda: int(input())
MII = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())

# def dfs(u, path): # recursive DFS 
#     path.append(u)
#     vis[u] = 1
#     if u == target:
#         return path
#     for v in adj[u]:
#         if not vis[v]:
#             dfs(v, path)

# In py use stack to avoid recursion limit
def dfs(start):
    stack = [start]
    path = []
    while stack:
        u = stack.pop()
        if vis[u]:
            continue
        vis[u] = 1
        path.append(u)
        if u == target:
            return path
        for v in adj[u]:
            if not vis[v]:
                stack.append(v)
    return path

# Build graph (adjacency list)
N = 200005
vis = [0 for _ in range(N)]
adj = defaultdict(list)
n, m = MII()
for _ in range(m):
    u, v = MII()  # for 0-index use GMI()
    adj[u].append(v)
    # adj[v].append(u) # iff undirected graph

start = 1
target = n
path = dfs(start)
