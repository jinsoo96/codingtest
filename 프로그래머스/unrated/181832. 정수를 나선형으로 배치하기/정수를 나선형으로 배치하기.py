def solution(n):
    matrix = [[0] * n for _ in range(n)]  # n x n 배열 생성
    num = 1  # 채워넣을 숫자 초기값
    row_start, row_end = 0, n - 1  # 행의 시작과 끝 인덱스
    col_start, col_end = 0, n - 1  # 열의 시작과 끝 인덱스

    while num <= n * n:
        # 왼쪽에서 오른쪽으로
        for i in range(col_start, col_end + 1):
            matrix[row_start][i] = num
            num += 1
        row_start += 1

        # 위에서 아래로
        for i in range(row_start, row_end + 1):
            matrix[i][col_end] = num
            num += 1
        col_end -= 1

        # 오른쪽에서 왼쪽으로
        for i in range(col_end, col_start - 1, -1):
            matrix[row_end][i] = num
            num += 1
        row_end -= 1

        # 아래에서 위로
        for i in range(row_end, row_start - 1, -1):
            matrix[i][col_start] = num
            num += 1
        col_start += 1

    return matrix
