n = int(input())
k = int(input())
apples = [list(map(int, input().split())) for _ in range(k)]
l = int(input())
directions = [list(input().split()) for _ in range(l)]

board = [[0] * n for _ in range(n)]
dummyDir = [[0] * n for _ in range(n)]  # 뱀의 이전 방향 기억
for apple in apples:
    board[apple[0] - 1][apple[1] - 1] = 1

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
curDir = 0
curHead = [0, 0]
curTail = [0, 0]
time = 0

while True:
    if curHead[0] < 0 or curHead[0] >= n or curHead[1] < 0 or curHead[1] >= n:
        break

    if board[curHead[0]][curHead[1]] == 1:
        board[curHead[0]][curHead[1]] = 2
        dummyDir[curHead[0]][curHead[1]] = curDir
        curHead[0] = curHead[0] + dx[curDir]
        curHead[1] = curHead[1] + dy[curDir]
    elif board[curHead[0]][curHead[1]] == 0:
        board[curHead[0]][curHead[1]] = 2
        dummyDir[curHead[0]][curHead[1]] = curDir
        curHead[0] = curHead[0] + dx[curDir]
        curHead[1] = curHead[1] + dy[curDir]

        if curHead != curTail:
            board[curTail[0]][curTail[1]] = 0
        prevDir = dummyDir[curTail[0]][curTail[1]]
        curTail[0] = curTail[0] + dx[prevDir]
        curTail[1] = curTail[1] + dy[prevDir]
    else:
        break
    time += 1

    if len(directions) != 0 and int(directions[0][0]) == time:
        if directions[0][1] == 'L':
            curDir = (curDir + 3) % 4
        else:
            curDir = (curDir + 1) % 4
        directions.pop(0)

print(time)

# N = int(input())
# K = int(input())
# matrix = [[0 for i in range(N)] for j in range(N)]
# for x in range(K):
#     a, b = map(int, input().split())
#     matrix[a-1][b-1] = 1
# L = int(input())
# move = []
# for y in range(L):
#     X, C = input().split()
#     move.append([int(X), C])
#
# time = 0
# dx = [0, 1, 0, -1]  # 동 / 남 / 서 / 북 순서
# dy = [1, 0, -1, 0]
# direction = 0  # 초기 방향 동쪽이므로..
# snake = [[0, 0]]
#
# while True:
#     nx = snake[0][0] + dx[direction]
#     ny = snake[0][1] + dy[direction]
#     snake.insert(0, [nx, ny])  # 뱀 리스트의 머리 설정
#     time += 1
#
#     if [nx, ny] in snake[1:]:  # 만약 머리가 새롭게 이동하려는 칸에 뱀의 몸체가 있다면
#         break
#     if nx < 0 or N <= nx or ny < 0 or N <= ny:  # 만약 머리가 새롭게 이동하려는 칸이 보드의 밖이라면
#         break
#     if matrix[nx][ny] == 0:  # 새롭게 앞으로 한 칸 이동한 경우
#         del snake[-1]  # 뱀 리스트의 꼬리 부분 삭제
#
#     if matrix[nx][ny] == 1:
#         matrix[nx][ny] = 0
#
#     if len(move) > 0:
#         if move[0][0] == time:
#             if move[0][1] == 'L':  # 왼쪽으로 회전할 차례라면
#                 if direction != 0:
#                     direction -= 1
#                 else:
#                     direction = 3
#             elif move[0][1] == 'D':  # 오른쪽으로 회전할 차례라면
#                 direction = (direction + 1) % 4
#             del move[0]
#             # 방향 설정 완료
#
# print(time)
