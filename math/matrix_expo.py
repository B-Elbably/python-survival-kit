# try to solve :
# 1- https://cses.fi/problemset/task/1722
# 2- https://cses.fi/problemset/task/1096

MOD = 10**9 + 7


def MulMat(a, b):
    n, m, k = len(a), len(b), len(b[0])

    ans = [[0] * k for _ in range(n)]

    for i in range(n):
        for j in range(k):
            for l in range(m):
                ans[i][j] += a[i][l] * b[l][j]
                ans[i][j] %= MOD
    return ans


def MatPower(a, n):
    ans = [[0] * len(a) for _ in range(len(a))]
    for i in range(len(a)):
        ans[i][i] = 1

    while n:
        if n & 1:
            ans = MulMat(ans, a)
        a = MulMat(a, a)
        n >>= 1

    return ans


n = int(input())  # power
base = []  # (m * m) matrix
ans = MatPower(base, n)  # Output: base^n mod MOD
print(ans)
