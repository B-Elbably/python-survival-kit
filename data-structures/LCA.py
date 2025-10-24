# LCA (Lowest Common Ancestor)
"""
    solve :
    https://cses.fi/problemset/task/1688
"""
import sys
input = lambda: sys.stdin.buffer.readline().decode().rstrip()

MAX_N = 200005
LOG_N = 20

up = [[0] * LOG_N for _ in range(MAX_N)]
adj = [[] for _ in range(MAX_N)]
d = [0] * MAX_N

def dfs(root=1):
    stack = [(root, 0)] 
    d[root] = 0

    while stack:
        u, p = stack.pop()
        up[u][0] = p
        
        if u != root:
            d[u] = d[p] + 1
        
        # Binary Lifting Precomputation
        for k in range(1, LOG_N):
            up[u][k] = up[up[u][k - 1]][k - 1]
        
        # Push children
        for v in adj[u]:
            if v != p:
                stack.append((v, u))

def get_kth_ancestor(u, k):
    if d[u] < k: 
        return -1 
    
    for i in range(LOG_N):
        if (k >> i) & 1: 
            u = up[u][i]
            if u == 0:
                break
    return u

def find_lca(a, b):
    if d[a] < d[b]:
        a, b = b, a
        
    a = get_kth_ancestor(a, d[a] - d[b])

    if a == b:
        return a

    # Binary Lift to find the LCA
    for i in range(LOG_N - 1, -1, -1):
        if up[a][i] != up[b][i]:
            a = up[a][i]
            b = up[b][i]
    
    return up[a][0]


# Build tree
n, q = map(int , input().split())
for i in range(n - 1):
    u , v = map(int , input().split())
    adj[u].append(v)

dfs(1)

# Queries
for _ in range(q):
    a, b = map(int, input().split())
    print(find_lca(a, b))

