# 문제 분석 못함 -> 한 선수에 대한 이긴 선수 + 진 선수 = 전체 - 1을 생각했으나 다른 것도 있다고 생각함
from collections import deque


def solution(n, results):
    answer = 0
    win = [[] for _ in range(n)]
    lose = [[] for _ in range(n)]

    for v, f in results:
        win[v - 1].append(f - 1)
        lose[f - 1].append(v - 1)

    for i in range(n):
        vCount = 0
        fCount = 0

        q = deque([i])
        visited = [False for _ in range(n)] # 4 - 3관계처럼 중복 횟수 제거
        while q:
            player = q.popleft()
            visited[player] = True
            for o in win[player]:
                if not visited[o]:
                    vCount += 1
                    visited[o] = True
                    q.append(o)

        q = deque([i])
        visited = [False for _ in range(n)]
        while q:
            player = q.popleft()
            visited[player] = True
            for x in lose[player]:
                if not visited[x]:
                    fCount += 1
                    visited[x] = True
                    q.append(x)

        if vCount + fCount == n - 1:
            answer += 1

    return answer


print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))
