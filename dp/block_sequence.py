
""" 
    recursion with memoization
    but python recursion limit is low
    so we use iterative approach.
    
    https://codeforces.com/contest/1881/problem/E
"""
 
# memo = {} # use defaultdict
# def dp(idx):
#     if idx > n: return float('inf')
#     if idx == n: return 0
#     if idx in memo: return memo[idx]

#     op1 = dp(idx + a[idx] + 1)
#     op2 = 1 + dp(idx + 1)
#     memo[idx] = min(op1, op2)
#     return memo[idx]

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    dp = [0] * (n + 1)
    dp[n - 1] = 1

    for i in range(n-2, -1, -1) :
        dp[i] = dp[i + 1] + 1
        if i + a[i] < n :
            dp[i] = min(dp[i], dp[i + a[i] + 1])

    print(dp[0])
