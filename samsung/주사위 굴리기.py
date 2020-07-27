N, M, x, y, K = map(int, input().split(' '))
matrix = [list(map(int, input().split(' '))) for _ in range(N)]
moves = list(map(int, input().split(' ')))

# 왼 위 오 아래
WE = [0] * 4

# 뒤 위 앞 아래
NS = [0] * 4

for move in moves:
    temp = [0] * 4
    if move == 1:
        if x + 1 < M:
            temp = WE.copy()
            for i in range(4):
                WE[i] = temp[i-1]
            x += 1
            if matrix[y][x] != 0:
                WE[3] = matrix[y][x]
                matrix[y][x] = 0
            else:
                matrix[y][x] = WE[3]
            NS[1] = WE[1]
            NS[3] = WE[3]
            print(NS[1])
    elif move == 2:
        if x - 1 >= 0:
            temp = WE.copy()
            for i in range(4):
                WE[i-1] = temp[i]
            x -= 1
            if matrix[y][x] != 0:
                WE[3] = matrix[y][x]
                matrix[y][x] = 0
            else:
                matrix[y][x] = WE[3]
            NS[1] = WE[1]
            NS[3] = WE[3]
            print(NS[1])
    elif move == 3:
        if y - 1 >= 0:
            temp = NS.copy()
            for i in range(4):
                NS[i - 1] = temp[i]
            y -= 1
            if matrix[y][x] != 0:
                NS[3] = matrix[y][x]
                matrix[y][x] = 0
            else:
                matrix[y][x] = NS[3]
            WE[1] = NS[1]
            WE[3] = NS[3]
            print(NS[1])
    elif move == 4:
        if y + 1 < N:
            temp = NS.copy()
            for i in range(4):
                NS[i] = temp[i-1]
            y += 1
            if matrix[y][x] != 0:
                NS[3] = matrix[y][x]
                matrix[y][x] = 0
            else:
                matrix[y][x] = NS[3]
            WE[1] = NS[1]
            WE[3] = NS[3]
            print(NS[1])