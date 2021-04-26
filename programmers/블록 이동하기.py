# check
# from collections import deque
#
#
# def can_move(cur1, cur2, new_board):
#     Y, X = 0, 1
#     cand = []
#     # 평행이동
#     DELTAS = [(-1, 0), (1, 0), (0, 1), (0, -1)]
#     for dy, dx in DELTAS:
#         nxt1 = (cur1[Y] + dy, cur1[X] + dx)
#         nxt2 = (cur2[Y] + dy, cur2[X] + dx)
#         if new_board[nxt1[Y]][nxt1[X]] == 0 and new_board[nxt2[Y]][nxt2[X]] == 0:
#             cand.append((nxt1, nxt2))
#     # 회전
#     if cur1[Y] == cur2[Y]:  # 가로방향 일 때
#         UP, DOWN = -1, 1
#         for d in [UP, DOWN]:
#             if new_board[cur1[Y] + d][cur1[X]] == 0 and new_board[cur2[Y] + d][cur2[X]] == 0:
#                 cand.append((cur1, (cur1[Y] + d, cur1[X])))
#                 cand.append((cur2, (cur2[Y] + d, cur2[X])))
#     else:  # 세로 방향 일 때
#         LEFT, RIGHT = -1, 1
#         for d in [LEFT, RIGHT]:
#             if new_board[cur1[Y]][cur1[X] + d] == 0 and new_board[cur2[Y]][cur2[X] + d] == 0:
#                 cand.append(((cur1[Y], cur1[X] + d), cur1))
#                 cand.append(((cur2[Y], cur2[X] + d), cur2))
#
#     return cand
#
#
# def solution(board):
#     # board 외벽 둘러싸기
#     N = len(board)
#     new_board = [[1] * (N + 2) for _ in range(N + 2)]
#     for i in range(N):
#         for j in range(N):
#             new_board[i + 1][j + 1] = board[i][j]
#
#     # 현재 좌표 위치 큐 삽입, 확인용 set
#     que = deque([((1, 1), (1, 2), 0)])
#     confirm = set([((1, 1), (1, 2))])
#
#     while que:
#         cur1, cur2, count = que.popleft()
#         if cur1 == (N, N) or cur2 == (N, N):
#             return count
#         for nxt in can_move(cur1, cur2, new_board):
#             if nxt not in confirm:
#                 que.append((*nxt, count + 1))
#                 confirm.add(nxt)

from collections import deque


def getMoveList(cur1, cur2, newBoard):
    cand = []
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(4):
        if newBoard[cur1[0] + dx[i]][cur1[1] + dy[i]] != 1 and newBoard[cur2[0] + dx[i]][cur2[1] + dy[i]] != 1:
            newCur1 = (cur1[0] + dx[i], cur1[1] + dy[i])
            newCur2 = (cur2[0] + dx[i], cur2[1] + dy[i])
            cand.append((newCur1, newCur2))

    if cur1[0] == cur2[0]:  # 가로에서 세로로 회전
        for d in [-1, 1]:
            if newBoard[cur1[0] + d][cur1[1]] != 1 and newBoard[cur2[0] + d][cur2[1]] != 1:
                cand.append(((cur1[0], cur1[1]), (cur1[0] + d, cur1[1])))
                cand.append(((cur2[0], cur2[1]), (cur2[0] + d, cur2[1])))
    else:
        for d in [-1, 1]:
            if newBoard[cur1[0]][cur1[1] + d] != 1 and newBoard[cur2[0]][cur2[1] + d] != 1:
                cand.append(((cur1[0], cur1[1]), (cur1[0], cur1[1] + d)))
                cand.append(((cur2[0], cur2[1]), (cur2[0], cur2[1] + d)))

    return cand


def solution(board):
    n = len(board)
    newBoard = [list([1] * (n + 2)) for _ in range(n + 2)]

    for i in range(n):
        newBoard[i + 1][1:n + 1] = board[i]

    q = deque([((1, 1), (1, 2), 0)])
    visited = set([((1, 1), (1, 2))])

    while q:
        cur1, cur2, count = q.popleft()
        if cur1 == (n, n) or cur2 == (n, n):
            return count

        for move in getMoveList(cur1, cur2, newBoard):
            if move not in visited:
                q.append((move[0], move[1], count + 1))
                visited.add(move)


print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))