# from copy import deepcopy
# from collections import deque

# n = int(input())
# block = [list(map(int, input().split())) for _ in range(n)]
# result = []
# direction = ['U', 'D', 'R', 'L']

# def calc(orders):
#     blockTemp = deepcopy(block)
#
#     for order in orders:
#         if order == 'L':
#             for i in range(n):
#                 q = deque([])
#                 for j in range(n):
#                     if blockTemp[i][j] != 0:
#                         q.append(blockTemp[i][j])
#                 s = deque([])
#                 if len(q) != 0:
#                     s = deque([q.popleft()])
#                 while len(q) != 0:
#                     a = s.pop()
#                     b = q.popleft()
#
#                     if a == b:
#                         s.append(a * 2)
#                     else:
#                         s.append(a)
#                         s.append(b)
#
#                 sLen = len(s)
#                 for j in range(sLen):
#                     blockTemp[i][j] = s[j]
#                 for j in range(sLen, n):
#                     blockTemp[i][j] = 0
#
#         if order == 'R':
#             for i in range(n):
#                 q = deque([])
#                 for j in range(n):
#                     if blockTemp[i][j] != 0:
#                         q.append(blockTemp[i][j])
#                 s = deque([])
#                 if len(q) != 0:
#                     s = deque([q.pop()])
#                 while len(q) != 0:
#                     a = s.pop()
#                     b = q.pop()
#
#                     if a == b:
#                         s.append(a * 2)
#                     else:
#                         s.append(a)
#                         s.append(b)
#
#                 sLen = len(s)
#                 for k in range(n - 1, n - sLen - 1, -1):
#                     blockTemp[i][k] = s.popleft()
#                 for w in range(n - sLen - 1, -1, -1):
#                     blockTemp[i][w] = 0
#
#         if order == 'U':
#             for i in range(n):
#                 q = deque([])
#                 for j in range(n):
#                     if blockTemp[j][i] != 0:
#                         q.append(blockTemp[j][i])
#                 s = deque([])
#                 if len(q) != 0:
#                     s.append(q.popleft())
#                 while len(q) != 0:
#                     a = s.pop()
#                     b = q.popleft()
#
#                     if a == b:
#                         s.append(a * 2)
#                     else:
#                         s.append(a)
#                         s.append(b)
#
#                 sLen = len(s)
#                 for j in range(sLen):
#                     blockTemp[j][i] = s[j]
#                 for j in range(sLen, n):
#                     blockTemp[j][i] = 0
#
#         if order == 'D':
#             for i in range(n):
#                 q = deque([])
#                 for j in range(n):
#                     if blockTemp[j][i] != 0:
#                         q.append(blockTemp[j][i])
#                 s = deque([])
#                 if len(q) != 0:
#                     s = deque([q.pop()])
#                 while len(q) != 0:
#                     a = s.pop()
#                     b = q.pop()
#
#                     if a == b:
#                         s.append(a * 2)
#                     else:
#                         s.append(a)
#                         s.append(b)
#
#                 sLen = len(s)
#                 for k in range(n - 1, n - sLen - 1, -1):
#                     blockTemp[k][i] = s.popleft()
#                 for w in range(n - sLen - 1, -1, -1):
#                     blockTemp[w][i] = 0
#
#     return blockTemp


from collections import deque


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
answer = 0
q = deque()


def get(i, j):
    if board[i][j]:
        q.append(board[i][j])
        board[i][j] = 0


def merge(i, j, di, dj):
    while q:
        x = q.popleft()
        if not board[i][j]:
            board[i][j] = x
        elif board[i][j] == x:
            board[i][j] = x * 2
            i, j = i + di, j + dj
        else:
            i, j = i + di, j + dj
            board[i][j] = x


def move(k):
    if k == 0:
        for j in range(n):
            for i in range(n):
                get(i, j)
            merge(0, j, 1, 0)
    elif k == 1:
        for j in range(n):
            for i in range(n - 1, -1, -1):
                get(i, j)
            merge(n -1, j, -1, 0)
    elif k == 2:
        for i in range(n):
            for j in range(n):
                get(i, j)
            merge(i, 0, 0, 1)
    else:
        for i in range(n):
            for j in range(n - 1,  -1, -1):
                get(i, j)
            merge(i, n -1, 0, -1)


def solve(count):
    global board, answer
    if count == 5:
        for i in range(n):
            answer = max(answer, max(board[i]))
        return

    b = [x[:] for x in board]

    for k in range(4):
        move(k)
        solve(count + 1)
        board = [x[:] for x in b]


solve(0)
print(answer)











