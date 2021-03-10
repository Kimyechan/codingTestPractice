from collections import deque

N, M = map(int, input().split())

matrix = [list(map(int, list(input()))) for _ in range(N)]

result = []

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

visited = [[False] * M for _ in range(N)]
dist = [[0] * M for _ in range(N)]
dist[0][0] = 1


def bfs(x, y):
    q = deque([[x, y]])

    while q:
        v = q.popleft()
        visited[v[0]][v[1]] = True
        for i in range(4):
            nx = v[0] + dx[i]
            ny = v[1] + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            if not visited[nx][ny] and matrix[nx][ny] == 1:
                visited[nx][ny] = True
                q.append([nx, ny])
                dist[nx][ny] = dist[v[0]][v[1]] + 1


bfs(0, 0)
print(dist[N-1][M-1])

# DFS 사용시 시간초과
# import sys
# sys.setrecursionlimit(100000)
#
# N, M = map(int, input().split())
#
# matrix = [list(map(int, list(input()))) for _ in range(N)]
#
# result = []
#
# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]
#
# visited = [[False] * M for _ in range(N)]

# minMove = sys.maxsize
#
#
# def dfs(x, y, move):
#     global minMove
#     if move > minMove:
#         return
#
#     if x == N-1 and y == M-1:
#         if minMove > move:
#             result.append(move)
#             minMove = move
#         return
#
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#
#         if nx < 0 or nx >= N or ny < 0 or ny >= M:
#             continue
#
#         if not visited[nx][ny] and matrix[nx][ny] == 1:
#             move += 1
#             visited[nx][ny] = True
#             dfs(nx, ny, move)
#             visited[nx][ny] = False
#             move -= 1
#
#
# dfs(0, 0, 0)
# print(minMove + 1)