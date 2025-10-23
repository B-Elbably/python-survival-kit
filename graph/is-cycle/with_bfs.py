# IDEA: Fast input/output
import sys

input = lambda: sys.stdin.buffer.readline().decode().rstrip()

# IDEA: Modules
from collections import defaultdict, deque

# IDEA: Simple to write Fast input/output
II = lambda: int(input())
MII = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())

# Check cycle using BFS (Kahn's algorithm - directed only)
def is_cycle_bfs(n, adj):
    indegree = [0] * (n + 1)
    for u in range(1, n + 1):
        for v in adj[u]:
            indegree[v] += 1
    
    queue = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            queue.append(i)
    
    count = 0
    while queue:
        u = queue.popleft()
        count += 1
        for v in adj[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)
    
    return count != n  # If not all visited, cycle exists



n, m = MII()
adj = defaultdict(list)
for _ in range(m):
    u, v = MII()
    adj[u].append(v)

if is_cycle_bfs(n, adj):
    print("Cycle exists")
else:
    print("No cycle")
