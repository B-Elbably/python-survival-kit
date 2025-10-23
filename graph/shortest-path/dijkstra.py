# IDEA: Fast input/output
import sys

input = lambda: sys.stdin.buffer.readline().decode().rstrip()

# IDEA: Modules
from collections import defaultdict
from heapq import heappop, heappush

# IDEA: Simple to write Fast input/output
II = lambda: int(input())
MII = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())

# Dijkstra's algorithm with weighted edges
def dijkstra(start, n, adj):
    dist = [-1] * (n + 1) # Distance array
    prev = [-1] * (n + 1) # To reconstruct path
    heap = [(0, start)]  # (distance, node)
    
    while heap:
        cost, u = heappop(heap)
        if dist[u] != -1:
            continue
        dist[u] = cost
        for v, w in adj[u]:
            if dist[v] == -1:
                heappush(heap, (cost + w, v))
                prev[v] = u
    return dist, prev

# Reconstruct path from start to target
def reconstruct_path(start, target, prev):
    path = []
    u = target
    while u != -1:
        path.append(u)
        u = prev[u]
    path.reverse()
    if path[0] != start:
        return []  # No path exists
    return path

# Build graph with weighted edges
n, m = MII()
adj = defaultdict(list)
for _ in range(m):
    u, v, w = MII()  # Read u, v, weight
    adj[u].append((v, w))
    adj[v].append((u, w))  # Remove if directed graph

start = 1
target = n

dist, prev = dijkstra(start, n, adj)
path = reconstruct_path(start, target, prev)

if path:
    print("Distance:", dist[target])
    print("Path:", *path)
else:
    print(-1)