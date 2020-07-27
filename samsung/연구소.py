from collections import deque
import copy

N, M = map(int, input().split(' '))
G = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

virusXMAX = 0


def block(lst):
    # list 복사 서로 영향 안주는 방법......!!!!!!!!!
    Temp = copy.deepcopy(G)
    clean = 0
    for spot in lst:
        Y = spot // M
        X = spot % M
        if G[Y][X] != 0:
            return 0
        else:
            Temp[Y][X] = 1

    for a in range(N):
        for b in range(M):
            if Temp[a][b] == 2:
                q = deque([[b, a]])

                while q:
                    v = q.popleft()
                    for k in range(4):
                        if 0 > v[0] + dx[k] or v[0] + dx[k] >= M or 0 > v[1] + dy[k] or v[1] + dy[k] >= N:
                            continue
                        else:
                            if Temp[v[1] + dy[k]][v[0] + dx[k]] == 0:
                                Temp[v[1] + dy[k]][v[0] + dx[k]] = 2
                                q.append([v[0] + dx[k], v[1] + dy[k]])

    for k in range(N):
        for l in range(M):
            if Temp[k][l] == 0:
                clean += 1
    return clean


for i in range(N*M):
    for j in range(i+1, N*M):
        for z in range(j+1, N*M):
            virusXMAX = max(virusXMAX, block([i, j, z]))

print(virusXMAX)