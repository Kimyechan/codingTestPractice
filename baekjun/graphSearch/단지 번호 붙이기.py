from collections import deque

N = int(input())

table = list()

table = [list(map(int, list(input()))) for _ in range(N)]
# for _ in range(N):
#     row = str(input())
#     temp = list()
#     for a in row:
#         temp.append(int(a))
#     table.append(temp)

visited = [[False] * N for _ in range(N)]

totalCount = 0
eachCountList = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(row, col):
    q = deque([[row, col]])
    eachCount = 1

    while q:
        v = q.popleft()
        visited[row][col] = True

        for i in range(4):
            nx = v[0] + dx[i]
            ny = v[1] + dy[i]

            if (N <= nx or nx < 0) or (N <= ny or ny < 0):
                continue

            if table[nx][ny] == 1 and visited[nx][ny] == False:
                visited[nx][ny] = True
                q.append([nx, ny])
                eachCount += 1

    return eachCount


for row in range(N):
    for col in range(N):
        if not visited[row][col] and table[row][col] == 1:
            result = bfs(row, col)
            eachCountList.append(result)
            totalCount += 1


print(totalCount)
eachCountList.sort()
for eachCount in eachCountList:
    print(eachCount)