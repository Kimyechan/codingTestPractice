from collections import deque

T = int(input())

move = [[1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1], [-2, 1], [-1, 2]]

for _ in range(T):
    N = int(input())
    start = list(map(int, input().split()))
    end = list(map(int, input().split()))

    visited = [list([False] * N) for _ in range(N)]
    dist = [list([0] * N) for _ in range(N)]


    def bfs():
        q = deque([start])
        visited[start[0]][start[1]] = True

        while q:
            v = q.popleft()

            if [v[0], v[1]] == end:
                print(dist[v[0]][v[1]])
                break

            for x, y in move:
                nx = v[0] + x
                ny = v[1] + y

                if nx >= N or nx < 0 or ny >= N or ny < 0:
                    continue

                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    dist[nx][ny] = dist[v[0]][v[1]] + 1
                    q.append([nx, ny])

    bfs()