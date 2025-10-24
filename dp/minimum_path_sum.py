"""
    Solve : https://leetcode.com/problems/minimum-path-sum?envType=problem-list-v2&envId=dynamic-programming
"""

II = lambda: int(input())
LII = lambda: list(map(int, input().split()))

grid = [LII for _ in range(II())]
n = len(grid)
m = len(grid[0])
dp = [[0] * m for _ in range(n)]
for j in range(1, m):
    dp[0][j] = dp[0][j-1] + grid[0][j]
    
for i in range(1, n):
    dp[i][0] = dp[i-1][0] + grid[i][0]
    
for i in range(1, n):
    for j in range(1, m):
        dp[i][j] = dp[i][j] + min(dp[i-1][j], dp[i][j-1])

print(dp[n-1][m-1])
