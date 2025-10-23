"""
    0/1 Knapsack Problem - Iterative DP solution
    problem : https://atcoder.jp/contests/dp/tasks/dp_d
"""

n, w = map(int, input().split())  # number of items, max weight
W = []  # weights
V = []  # values
for _ in range(n):
    wi, vi = map(int, input().split())
    W.append(wi)
    V.append(vi)

# dp[i][j] = max value using first i items with total weight <= j
dp = [[0] * (w + 1) for _ in range(n + 1)]


for i in range(1, n + 1):
    for j in range(w + 1):
        # Option 1: skip
        dp[i][j] = dp[i - 1][j]

        # Option 2: take item (if fits)
        if j >= W[i - 1]:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - W[i - 1]] + V[i - 1])

print(dp[n][w])


"""
    You can search about fractional knapsack and unbounded knapsack.
    Have a good day!
"""