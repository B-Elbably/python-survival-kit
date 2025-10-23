# IDEA: Fast input/output
import sys

input = lambda: sys.stdin.buffer.readline().decode().rstrip()

# IDEA: Modules
from collections import defaultdict, deque

# IDEA: Simple to write Fast input/output
II = lambda: int(input())
MII = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())


def topological_sort(n, adj):
    indegree = [0] * (n + 1)
    for u in range(1, n + 1):
        for v in adj[u]:
            indegree[v] += 1

    queue = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            queue.append(i)

    topo_order = []
    while queue:
        u = queue.popleft()
        topo_order.append(u)
        for v in adj[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)

    if len(topo_order) != n:
        return [] # Not topologically sortable (cycle detected)
    return topo_order


# build graph (adjacency list)
N = 200005
vis = [0 for _ in range(N)]
adj = defaultdict(list)
n, m = MII()
for _ in range(m):
    u, v = MII()  # for 0-index use GMI()
    adj[u].append(v)
    # adj[v].append(u) # Must be directed graph

topo = topological_sort(n, adj)
if not topo:
    print("Graph has a cycle")
else:
    print("Topological order:", topo)

"""
    Search "Topological Sort" for more details.
    Implement using DFS also.
"""