import sys
n, m = map(int, input().split())

board = [list(input()) for _ in range(n)]

minChange = sys.maxsize
for startRow in range(len(board) - 7):
    for startCol in range(len(board[startRow]) - 7):
        for color in [1, -1]:
            change = 0
            for i in range(8):
                for j in range(8):
                    if board[startRow + i][startCol + j] == 'B' and color == 1:
                        change += 1
                    elif board[startRow + i][startCol + j] == 'W' and color == -1:
                        change += 1
                    color *= -1
                color *= -1
            minChange = min(minChange, change)

print(minChange)
