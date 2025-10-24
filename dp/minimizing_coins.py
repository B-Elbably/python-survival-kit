"""
    https://cses.fi/problemset/task/1634/
"""

n, x = map(int, input().split())
a = list(map(int, input().split()))

MAX_N = 10**6
INF = 10**9

dp = [INF] * (MAX_N + 1)
dp[0] = 1  # base case 

for i in range(MAX_N + 1):
    if dp[i] == INF: continue
    
    for now in a:
        if i + now <= MAX_N:
            dp[i + now] = min(dp[i + now], dp[i] + 1)

print(dp[x] - 1 if dp[x] != INF else -1)

