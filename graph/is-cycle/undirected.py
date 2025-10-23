"""
    track parent to detect back edges
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

# Check cycle in undirected graph using DFS
def is_cycle_undirected(n, adj):
    visited = [False] * (n + 1)
    
    def dfs(u, parent):
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                if dfs(v, u):
                    return True
            elif v != parent:  # Back edge to non-parent
                return True
        return False
    
    for i in range(1, n + 1):
        if not visited[i]:
            if dfs(i, -1):
                return True
    return False


# Example usage:
n, m = MII()
adj = defaultdict(list)

for _ in range(m):
    u, v = MII()
    # build undirected adjacency
    adj[u].append(v)
    adj[v].append(u)


if is_cycle_undirected(n, adj):
    print("Cycle exists")
else:
    print("No cycle")

