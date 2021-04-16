n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

# 회전 y * -1, 후에 x, y 변경
blocks = [[[0, 0], [0, - 1], [0, -2], [1, -2]],
          [[0, 0], [1, 0], [2, 0], [3, 0]],
          [[0, 0], [1, 0], [0, -1], [1, -1]],
          [[0, 0], [0, -1], [1, -1], [1, -2]],
          [[0, 0], [1, 0], [2, 0], [1, -1]]]

blockMaxSum = 0


def calcMaxSum():
    global block, i, blockMaxSum
    for mode in range(4):
        for y in range(n):
            for x in range(m):
                for block in blocks:
                    flag = 0
                    blockSum = 0
                    for i in range(4):
                        nx = x + block[i][0]
                        ny = y + block[i][1]
                        if nx < 0 or nx >= m or ny < 0 or ny >= n:
                            flag = 1
                            break
                        blockSum += board[ny][nx]
                    if flag == 0:
                        blockMaxSum = max(blockMaxSum, blockSum)
        for block in blocks:
            for i in range(4):
                block[i][0], block[i][1] = -block[i][1], block[i][0]


calcMaxSum()

# 대칭 이동
for block in blocks:
    for i in range(4):
        block[i][1] = -block[i][1]

calcMaxSum()

print(blockMaxSum)


# n, m = map(int, input().split())
# board = [list(map(int, input().split())) for _ in range(n)]
#
# blocks = [
#     [(0, 0), (0, 1), (1, 0), (1, 1)],  # ㅁ
#     [(0, 0), (0, 1), (0, 2), (0, 3)],  # ㅡ
#     [(0, 0), (1, 0), (2, 0), (3, 0)],  # ㅣ
#     [(0, 0), (0, 1), (0, 2), (1, 0)],
#     [(1, 0), (1, 1), (1, 2), (0, 2)],
#     [(0, 0), (1, 0), (1, 1), (1, 2)],  # ㄴ
#     [(0, 0), (0, 1), (0, 2), (1, 2)],  # ㄱ
#     [(0, 0), (1, 0), (2, 0), (2, 1)],
#     [(2, 0), (2, 1), (1, 1), (0, 1)],
#     [(0, 0), (0, 1), (1, 0), (2, 0)],
#     [(0, 0), (0, 1), (1, 1), (2, 1)],
#     [(0, 0), (0, 1), (0, 2), (1, 1)],  # ㅜ
#     [(1, 0), (1, 1), (1, 2), (0, 1)],  # ㅗ
#     [(0, 0), (1, 0), (2, 0), (1, 1)],  # ㅏ
#     [(1, 0), (0, 1), (1, 1), (2, 1)],  # ㅓ
#     [(1, 0), (2, 0), (0, 1), (1, 1)],
#     [(0, 0), (1, 0), (1, 1), (2, 1)],
#     [(1, 0), (0, 1), (1, 1), (0, 2)],
#     [(0, 0), (0, 1), (1, 1), (1, 2)]
# ]
#
# blockMaxSum = 0
# for y in range(n):
#     for x in range(m):
#         for block in blocks:
#             flag = 0
#             blockSum = 0
#             for i in range(4):
#                 nx = x + block[i][0]
#                 ny = y + block[i][1]
#                 if nx < 0 or nx >= m or ny < 0 or ny >= n:
#                     flag = 1
#                     break
#                 blockSum += board[ny][nx]
#             if flag == 0:
#                 blockMaxSum = max(blockMaxSum, blockSum)
#
# print(blockMaxSum)
