from collections import defaultdict
from collections import deque


K = int(input())

for _ in range(K):
    V, E = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(E)]

    table = defaultdict(list)

    for v1, v2 in graph:
        table[v1-1].append(v2-1)
        table[v2-1].append(v1-1)

    visited = [False] * V
    color = [0] * V
    result = True

    def bfs(start, visited, color):
        global result
        q = deque([start])
        visited[start] = True
        color[start] = 1

        while q and result:
            v = q.popleft()

            for adj in table[v]:
                if visited[adj] and color[v] == color[adj]:
                    result = False
                    break
                elif not visited[adj]:
                    visited[adj] = True
                    color[adj] = -1 * color[v]
                    q.append(adj)


    for i in range(V):
        if not visited[i]:
            visited = [False] * V
            color = [0] * V
            bfs(i, visited, color)
        if not result:
            break

    if result:
        print("YES")
    else:
        print("NO")