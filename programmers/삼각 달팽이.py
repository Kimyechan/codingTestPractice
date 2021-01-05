def solution(n):
    answer = []
    dx = [1, 0, -1] # 삼각형 세 방향으로 이동
    dy = [0, 1, -1]
    board = [[0] * n for _ in range(n)]

    cnt = 1
    i, j = 0, 0
    d = 0
    distance = n * (n + 1) // 2

    while distance >= cnt:
        if 0 <= i < n and 0 <= j < n and board[i][j] == 0:
            board[i][j] = cnt
            cnt += 1
        else:
            i -= dx[d]
            j -= dy[d]
            d = (d + 1) % 3
        i += dx[d]
        j += dy[d]

    for i in range(n):
        for j in range(0, i + 1):
            answer.append(board[i][j])
    return answer

print(solution(4))