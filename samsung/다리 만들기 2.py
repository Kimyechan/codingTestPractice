from collections import deque
import heapq

N, M = map(int, input().split())
landMap = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs():
    visited = [list([False] * M) for _ in range(N)]
    land = []

    for i in range(N):
        for j in range(M):
            country = []
            if landMap[i][j] == 1 and not visited[i][j]:
                q = deque([[i, j]])
                visited[i][j] = True
                country.append([i, j])

                while q:
                    v = q.popleft()

                    for k in range(4):
                        nx = v[0] + dx[k]
                        ny = v[1] + dy[k]

                        if nx >= N or nx < 0 or ny >= M or ny < 0:
                            continue

                        if not visited[nx][ny] and landMap[nx][ny] == 1:
                            q.append([nx, ny])
                            visited[nx][ny] = True
                            country.append([nx, ny])

                land.append(country)

    return land


landPosList = bfs()
edges = []

for i in range(len(landPosList)):
    for spot in landPosList[i]:
        for j in range(4):
            dis = 0
            flag = 0
            start = spot
            while 0 <= start[0] + dx[j] < N and 0 <= start[1] + dy[j] < M:
                nx = start[0] + dx[j]
                ny = start[1] + dy[j]
                dis += 1

                if [nx, ny] in landPosList[i] and landMap[nx][ny] == 1:
                    break

                if [nx, ny] not in landPosList[i] and landMap[nx][ny] == 1:
                    for k in range(len(landPosList)):
                        flag = 1
                        if [nx, ny] in landPosList[k] and dis - 1 >= 2:
                            edges.append([dis - 1, i, k])
                            break

                if flag == 1:
                    break

                start = [nx, ny]

parent = [i for i in range(len(landPosList))]
rank = [0] * len(landPosList)


def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]


def union(n1, n2):
    p1 = find(n1)
    p2 = find(n2)

    if rank[p1] > rank[p2]:
        parent[p2] = p1
    else:
        parent[p1] = p2
        if rank[p1] == rank[p2]:
            rank[p2] += 1


def kruskal(edgeList):
    heapq.heapify(edgeList)
    totalLen = 0

    while edgeList:
        edge = heapq.heappop(edgeList)

        if find(edge[1]) != find(edge[2]):
            union(edge[1], edge[2])
            totalLen += edge[0]

    return totalLen


result = kruskal(edges)
count = 0
for i in range(len(landPosList)):
    if parent[i] == i:
        count += 1
if count >= 2:
    print(-1)
else:
    print(result)










