from collections import deque


def solution(n, edges):
    answer = 0
    vertex = list([] for _ in range(n + 1))
    for edge in edges:
        vertex[edge[0]].append(edge[1])
        vertex[edge[1]].append(edge[0])

    minD = [0 for _ in range(n + 1)]
    visited = [False for _ in range(n + 1)]

    q = deque([1])
    visited[1] = True
    prev = [0 for _ in range(n+1)]

    while q:
        v = q.popleft()
        for adj in vertex[v]:
            if not visited[adj]:
                visited[adj] = True
                q.append(adj)
                prev[adj] = v
                minD[adj] = minD[prev[adj]] + 1

    maxValue = max(minD)
    for dis in minD:
        if dis == maxValue:
            answer += 1

    return answer


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))