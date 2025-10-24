"""
    https://codeforces.com/contest/1926/problem/C
"""
MAXN = 200000 # 2e5
dp = [0] * (MAXN + 1)
for i in range(1, MAXN + 1):
    g = 0
    ref = i
    while ref:
        g += ref % 10
        ref //= 10
    dp[i] = (dp[i-1] + g)

for _ in range(int(input())):
    n = int(input())
    print(dp[n])