# Longest Common Subsequence (LCS)
# This version on string (not array of numbers)

"""
    Find the Longest Common Subsequence (LCS) between two strings s and t.
    problem : https://atcoder.jp/contests/dp/tasks/dp_f
"""

def lcs(s, t):
    n, m = len(s), len(t)
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)] # dp[n][m]
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s[i - 1] == t[j - 1]: # match ?
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Reconstruct LCS (Traceback)
    result = []
    i, j = n, m
    while i > 0 and j > 0:
        if s[i - 1] == t[j - 1]: # match ?
            result.append(s[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]: # go up
            i -= 1
        else: # go left
            j -= 1
    
    return ''.join(result[::-1])

s = input().strip() # first string
t = input().strip() # second string

ans = lcs(s, t)
print("Length of LCS:", len(ans))
print("LCS:", ans)