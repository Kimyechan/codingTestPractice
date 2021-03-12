from collections import deque


M, N = map(int, input().split())

box = [list(map(int, input().split())) for _ in range(N)]

visited = [[False] * M for _ in range(N)]
past = [[0] * M for _ in range(N)]

q = deque([])

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs():
    while q:
        v = q.popleft()

        for i in range(4):
            nx = v[0] + dx[i]
            ny = v[1] + dy[i]

            if nx >= N or nx < 0 or ny >= M or ny < 0:
                continue

            if not visited[nx][ny] and box[nx][ny] == 0:
                past[nx][ny] = past[v[0]][v[1]] + 1
                visited[nx][ny] = True
                q.append([nx, ny])


count1 = 0
count2 = 0
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            visited[i][j] = True
            past[i][j] = 1
            q.append([i, j])
            count1 += 1
        elif box[i][j] == -1:
            past[i][j] = -1
            count2 += 1

if count1+count2 == N * M:
    print(0)
else:
    bfs()
    flag = 1
    maxPast = 0
    for i in range(N):
        for j in range(M):
            if past[i][j] == 0:
                flag = 0
            if maxPast < past[i][j]:
                maxPast = past[i][j]
    if flag == 1:
        print(maxPast-1)
    else:
        print(-1)
