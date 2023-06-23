def solution(board, k):
    n = len(board)
    m = len(board[0])

    total = 0
    for i in range(n):
        for j in range(m):
            if i + j <= k:
                total += board[i][j]

    return total