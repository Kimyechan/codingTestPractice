# check
from collections import deque, defaultdict


def solution(arrows):
    arrows.append(4)
    answer = 0

    q = deque([])
    visited = defaultdict(int)
    visitedPath = defaultdict(int)

    move = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

    x, y = 0, 0
    for arrow in arrows:
        for _ in range(2):
            x += move[arrow][0]
            y += move[arrow][1]
            q.append((x, y))

    now = (0, 0)
    visited[now] = 1

    while q:
        next = q.popleft()

        if visited[next] == 1:
            if visitedPath[(now, next)] == 0:
                answer += 1
        else:
            visited[next] = 1

        visitedPath[(now, next)] = 1
        visitedPath[(next, now)] = 1
        now = next

    return answer


print(solution([6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]))