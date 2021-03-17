from copy import deepcopy
board = [list(map(int, input().split())) for _ in range(9)]
candidate = []

for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            candidate.append([i, j])


def isAvailable(level, num, board):
    row, col = candidate[level]

    if num in board[row]:
        return False

    for boardLine in board:
        if num == boardLine[col]:
            return False

    secRow = row // 3
    secCol = col // 3
    for i in range(secRow * 3, (secRow + 1) * 3):
        for j in range(secCol * 3, (secCol + 1) * 3):
            if num == board[i][j]:
                return False

    return True


result = []


def backTracking(level, board):
    if len(result) == 1:
        return

    if level == len(candidate):
        result.append(deepcopy(board))
        return

    for num in range(1, 10):
        [i, j] = candidate[level]
        if isAvailable(level, num, board):
            board[i][j] = num
            backTracking(level + 1, board)
            board[i][j] = 0


backTracking(0, board)
for i in range(9):
    for j in range(9):
        print(result[0][i][j], end=" ")
    print()