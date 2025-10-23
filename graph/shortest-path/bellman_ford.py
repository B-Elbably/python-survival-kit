# IDEA: Fast input/output
import sys

input = lambda: sys.stdin.buffer.readline().decode().rstrip()

# IDEA: Simple to write Fast input/output
II = lambda: int(input())
MII = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())

# Bellman-Ford algorithm
def BellmanFord(src, n, edges):
    INF = 10**15
    dist = [INF] * (n + 5)
    dist[src] = 0
    ok = False
    
    for i in range(n):
        for u, v, w in edges:
            if dist[u] != INF and dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                if v == n and i == n - 1:
                    ok = True
    
    if ok:
        return -10**15  # negative cycle
    return dist[n]

# Read input
n, m = MII()
edges = []
for _ in range(m):
    u, v, w = MII()
    edges.append((u, v, w))

start = 1
result = BellmanFord(start, n, edges)

if result == -10**15:
    print("Negative cycle detected")
else:
    print(result)