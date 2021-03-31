from collections import deque
import sys

n = int(sys.stdin.readline())

tree = [[] for _ in range(n + 1)]
for _ in range(n):
    info = list(map(int, sys.stdin.readline().split()))
    value = info[1]
    index = 1
    v = 0
    w = 0
    while value !=- 1:
        if index % 2 == 1:
            v = info[index]
        else:
            w = info[index]
            tree[info[0]].append([v, w])
        index += 1
        value = info[index]


def bfs(node):
    visited = [False] * (n + 1)
    dist = [0] * (n + 1)
    q = deque([[node, 0]])

    while q:
        vertex, weight = q.popleft()
        visited[vertex] = True

        for nextV, nextW in tree[vertex]:
            if not visited[nextV]:
                visited[nextV] = True
                dist[nextV] = weight + nextW
                q.append((nextV, dist[nextV]))

    maxDis = max(dist)
    v = dist.index(maxDis)

    return maxDis, v


vertex = bfs(1)[1]
result = bfs(vertex)[0]

print(result)

