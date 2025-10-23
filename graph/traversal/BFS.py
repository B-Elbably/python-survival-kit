# IDEA: Fast input/output
import sys

input = lambda: sys.stdin.buffer.readline().decode().rstrip()

# IDEA: Modules
from collections import deque,defaultdict

# IDEA: Simple to write Fast input/output
II = lambda: int(input())
MII = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())

def bfs(start):
    queue = deque([start])
    path = []
    vis[start] = 1
    while queue:
        u = queue.popleft()
        path.append(u)
        if u == target:
            return path
        for v in adj[u]:
            if not vis[v]:
                vis[v] = 1
                queue.append(v)
    return path


# Build graph (adjacency list)
N = 200005
adj = defaultdict(list)
vis = [0 for _ in range(N)]
n, m = MII()
for _ in range(m):
    u, v = MII()  # for 0-index use GMI()
    adj[u].append(v)
    adj[v].append(u)

start = 1
target = n
path = bfs(start)
