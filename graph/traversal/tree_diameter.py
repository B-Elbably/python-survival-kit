# There is two ways
# 1- Make two DFS to find tree diameter

"""
    ببساطة الفكرة :
    تعريفه : طول أطول مسار بين أي نقطتين.
    
    الطريقة الأولى (المستخدمة هنا) :
    1-DFS من أي نقطة عشوائية 
    2-تحديد أبعد نقطة من النقطة التي بدأنا منها (نسميها A)
    3-DFS من النقطة A لتحديد أبعد نقطة منها (نسميها B)
    4- المسافة بين (A , B) هي .
"""

import sys
from collections import defaultdict

input = lambda: sys.stdin.buffer.readline().decode().rstrip()
II = lambda: int(input())
MII = lambda: map(int, input().split())
GMI = lambda: map(lambda x: int(x) - 1, input().split())

def dfs_stack(start, n, adj):
    stack = [(start, 0)]
    vis = [0] * (n + 1)
    mx = 0
    farthest_node = start
    
    while stack:
        u, depth = stack.pop()
        if vis[u]:
            continue
        vis[u] = 1
        
        if depth > mx:
            mx = depth
            farthest_node = u
        
        for v in adj[u]:
            if not vis[v]:
                stack.append((v, depth + 1))
    
    return farthest_node, mx

n = II()
adj = defaultdict(list)

for _ in range(n - 1):
    u, v = MII()
    adj[u].append(v)
    adj[v].append(u)

# First DFS to find farthest node from arbitrary node (1)
farthest, _ = dfs_stack(1, n, adj)

# Second DFS to find diameter from that farthest node
_, diameter = dfs_stack(farthest, n, adj)

print(diameter)


"""
    Search about Second method
    Dr.Mostafa Saad (YouTube channel) has explained it well.
"""

