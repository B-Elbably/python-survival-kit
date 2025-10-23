# IDEA: Fast input/output
import sys

input = lambda: sys.stdin.buffer.readline().decode().rstrip()

# IDEA: Modules
from collections import defaultdict

# IDEA:
II = lambda: int(input())
MII = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())

N = 200005
vis = [0 for _ in range(N)]


def dfs(u, path):
    path.append(u)
    vis[u] = 1
    if u == target:
        return path
    for v in adj[u]:
        if not vis[v]:
            dfs(v, path)


adj = defaultdict(list)
n, m = MII()
for _ in range(m):
    u, v = MII()  # for 0-index use GMI()
    adj[u].append(v)
    adj[v].append(u)

start = 1
target = n
path = dfs(start)
