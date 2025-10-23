# IDEA: Fast input/output
import sys
input = lambda: sys.stdin.buffer.readline().decode().rstrip()

# IDEA: Modules
from collections import defaultdict
from heapq import heappop, heappush

# IDEA: Simple to write Fast input/output
MII = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())

# Prim's MST Algorithm using heapq
def prim(n, adj):
    visited = [False] * (n + 1)
    min_heap = [(0, 1, -1)]  # (weight, current_node, parent)
    total_weight = 0
    mst_edges = []
    
    while min_heap and len(mst_edges) < n - 1:
        w, u, parent = heappop(min_heap)
        if visited[u]:
            continue
        visited[u] = True
        total_weight += w
        if parent != -1:
            mst_edges.append((parent, u, w))
        
        for v, weight in adj[u]:
            if not visited[v]:
                heappush(min_heap, (weight, v, u))
    
    if len(mst_edges) != n - 1:
        return -1, []  # No MST
    return total_weight, mst_edges


n, m = MII()
adj = defaultdict(list)

for _ in range(m):
    u, v, w = MII()
    adj[u].append((v, w))
    adj[v].append((u, w))  # Undirected graph

weight, mst = prim(n, adj)

if weight == -1:
    print("No MST exists")
else:
    print("MST weight:", weight)
    print("MST edges:")
    for u, v, w in mst:
        print(u, v, w)
        
        
"""
    Search about Kruskal's Algorithm
"""