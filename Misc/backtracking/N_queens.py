def is_valid(row, col, n, board):
    for i in range(row):
        if board[i][col] == "Q":
            return False
    
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == "Q":
            return False
        i -= 1
        j -= 1
    
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == "Q":
            return False
        i -= 1
        j += 1
    
    return True

def backtrack(row, n, board, ans):
    if row == n:
        ans.append([''.join(r) for r in board])
        return
    
    for col in range(n):
        if is_valid(row, col, n, board):
            board[row][col] = "Q"
            backtrack(row + 1, n, board, ans)
            board[row][col] = "."

# T.C = O(N!)
# S.C = O(N^2) for board + O(N) for recursion stack

n = 4 # n up to 11 
board = [["." for _ in range(n)] for _ in range(n)] # board[n][n]
ans = []
backtrack(0, n, board, ans)
print("Total solutions:", len(ans))

# for sol in ans:
#     for i in sol:
#         print(i)
#     print()

"""
    N-Queens Problem (Leetcode)
    Search about optimizations of this approach.
"""