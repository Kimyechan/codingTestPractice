from collections import deque

M, N, H = map(int, input().split())

box = [list() for _ in range(H)]
for i in range(H):
    box[i] = [list(map(int, input().split())) for _ in range(N)]

q = deque([])
visited = [list(list([False] * M) for _ in range(N)) for _ in range(H)]

for i in range(H):
    for j in range(N):
        for k in range(M):
            if box[i][j][k] == 1:
                q.append([i, j, k])

dh = [0, 0, 0, 0, 1, -1]
dn = [0, 0, 1, -1, 0, 0]
dm = [1, -1, 0, 0, 0, 0]


def bfs():
    while q:
        v = q.popleft()

        for i in range(6):
            nh = v[0] + dh[i]
            nn = v[1] + dn[i]
            nm = v[2] + dm[i]

            if nh >= H or nh < 0 or nn >= N or nn < 0 or nm >= M or nm < 0:
                continue

            if not visited[nh][nn][nm] and box[nh][nn][nm] == 0:
                visited[nh][nn][nm] = True
                q.append([nh, nn, nm])
                box[nh][nn][nm] = box[v[0]][v[1]][v[2]] + 1


bfs()
flag = 1
maxPast = 0

for i in range(H):
    for j in range(N):
        for k in range(M):
            if box[i][j][k] == 0:
                flag = 0
                break
            temp = max(box[i][j])
            if temp > maxPast:
                maxPast = temp

if flag == 0:
    print(-1)
else:
    print(maxPast - 1)