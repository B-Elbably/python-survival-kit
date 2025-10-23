# IDEA: Fast input/output
import sys

input = lambda: sys.stdin.buffer.readline().decode().rstrip()

# IDEA: Simple to write Fast input/output
II = lambda: int(input())
MII = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())

# Floyd-Warshall algorithm
def floyd_warshall(n, edges):
    INF = 10**15
    dist = [[INF] * (n + 1) for _ in range(n + 1)]
    
    # diagonal to 0
    for i in range(1, n + 1):
        dist[i][i] = 0
    
    for u, v, w in edges:
        dist[u][v] = min(dist[u][v], w)
        # dist[v][u] = min(dist[v][u], w) # undirected graph
    
    # main algorithm
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if dist[i][k] != INF and dist[k][j] != INF:
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    for i in range(1, n + 1):
        if dist[i][i] < 0:
            return None  # Negative cycle detected
    
    return dist

# Read input
n, m = MII()
edges = []
for _ in range(m):
    u, v, w = MII()
    edges.append((u, v, w))

distance = floyd_warshall(n, edges)

if distance is None:
    print("Negative cycle detected")
else:
    # Print all pairs shortest path
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if distance[i][j] == 10**15:
                print("INF", end=" ")
            else:
                print(distance[i][j], end=" ")
        print()