"""
    https://cses.fi/problemset/task/1637/
"""

MAX_N = 10**4
INF = 10**9
dp = [INF] * (MAX_N + 1)

def go():
    dp[0] = 0
    for i in range(1, MAX_N + 1):
        ref = i
        while ref:
            dp[i] = min(dp[i], 1 + dp[i - ref % 10])
            ref //= 10

go()

n = int(input())
print(dp[n])
