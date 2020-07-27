from collections import deque
test_case = int(input())
for _ in range(test_case):
    M, N, K = map(int, input().split(' '))

    bechu = [list(map(int, input().split())) for i in range(K)]

    # [[0] * M] * N => [0] * M 복사 N 한 행의 변화가 전부 변화함
    matrix = [[0] * M for _ in range(N)]

    for spot in bechu:
        matrix[spot[1]][spot[0]] = 1

    protect = [[False] * M for _ in range(N)]
    needJiRung = 0

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]


    def bp(x, y):
        q = deque([(x, y)])
        protect[y][x] = True

        while q:
            (a, b) = q.popleft()
            for i in range(4):
                if b + dy[i] >= N or b + dy[i] < 0 or a + dx[i] >= M or a + dx[i] < 0:
                    continue
                if matrix[b + dy[i]][a + dx[i]] == 1 and not protect[b + dy[i]][a + dx[i]]:
                    q.append((a + dx[i], b + dy[i]))
                    protect[b + dy[i]][a + dx[i]] = True


    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 1 and not protect[i][j]:
                bp(j, i)
                needJiRung += 1

    print(needJiRung)


