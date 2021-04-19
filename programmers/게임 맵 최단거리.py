from collections import deque


def solution(maps):
    n = len(maps)
    m = len(maps[0])
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    q = deque([(0, 0)])
    visited = [list([False] * m) for _ in range(n)]
    visited[0][0] = True
    distances = [list([1] * m) for _ in range(n)]

    while q:
        node = q.popleft()

        for i in range(4):
            nx = node[0] + dx[i]
            ny = node[1] + dy[i]

            if nx >= n or nx < 0 or ny >= m or ny < 0:
                continue

            if maps[nx][ny] == 1 and not visited[nx][ny]:
                distances[nx][ny] = distances[node[0]][node[1]] + 1
                visited[nx][ny] = True
                q.append((nx, ny))

    if distances[n - 1][m - 1] != 1:
        answer = distances[n - 1][m - 1]
    else:
        answer = - 1

    return answer


print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]))
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))
