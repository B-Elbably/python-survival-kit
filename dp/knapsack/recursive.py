"""
    0/1 Knapsack Problem - Recursive DP solution with memoization
    problem : https://atcoder.jp/contests/dp/tasks/dp_d
"""


n, w = map(int, input().split()) # number of items, max weight
W = [] # weights
V = [] # values
for _ in range(n):
    wi, vi = map(int, input().split())
    W.append(wi)
    V.append(vi)

# Initialize DP table with -1
dp = [[-1] * (w + 1) for _ in range(n + 1)]

def solve(i, rem):
    if rem == 0 or i == n:
        return 0
    if dp[i][rem] != -1:
        return dp[i][rem]

    # Option 1: skip 
    res = solve(i + 1, rem)

    # Option 2: take (if it fits)
    if rem >= W[i]:
        res = max(res, solve(i + 1, rem - W[i]) + V[i])

    dp[i][rem] = res
    return res

print(solve(0, w))


"""
    Learn more about recursion tree and memoization.
"""
