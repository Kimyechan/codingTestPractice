from collections import deque

N, M = map(int, input().split())

matrix = [list(map(int, list(input()))) for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
visited = [[[False] * 2 for _ in range(M)] for _ in range(N)]
dist = [[[0] * 2 for _ in range(M)] for _ in range(N)]

visited[0][0][0] = True
dist[0][0][0] = 1


def bfs():
    q = deque([[0, 0, 0]])

    while q:
        v = q.popleft()

        for i in range(4):
            nx = v[0] + dx[i]
            ny = v[1] + dy[i]

            if nx >= N or nx < 0 or ny >= M or ny < 0:
                continue

            if matrix[nx][ny] == 0 and not visited[nx][ny][v[2]]:
                visited[nx][ny][v[2]] = True
                dist[nx][ny][v[2]] = dist[v[0]][v[1]][v[2]] + 1
                q.append([nx, ny, v[2]])
            elif v[2] == 0 and matrix[nx][ny] == 1 and not visited[nx][ny][v[2]]:
                visited[nx][ny][1] = True
                dist[nx][ny][1] = dist[v[0]][v[1]][v[2]] + 1
                q.append([nx, ny, 1])

    return dist[N-1][M-1]


result = bfs()
minRoute = min(bfs())

if minRoute == 0:
    count = 0
    for i in range(2):
        if result[i] != 0:
            print(result[i])
        else:
            count += 1
    if count == 2:
        print(-1)
else:
    print(minRoute)