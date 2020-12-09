# dictionary key 값을 튜플로 둘 수 있음

from collections import deque
from collections import defaultdict


def solution(arrows):
    answer = 0
    mX = [0, 1, 1, 1, 0, -1, -1, -1]
    mY = [1, 1, 0, -1, -1, -1, 0, 1]

    vertex = defaultdict(int)
    edge = defaultdict(int)
    q = deque([[0, 0]])
    x, y = 0, 0

    # 홀수 길이 일 때 X 자로 만나면 X 교차점이 정점으로 나타나지 않아서 카운트가 되지 않는다
    # 전체 이동을 2배 늘려준다
    for arrow in arrows:
        for _ in range(2):
            nx = x + mX[arrow]
            ny = y + mY[arrow]
            q.append([nx, ny])
            x, y = nx, ny

    x, y = q.popleft()
    vertex[(x, y)] = 1

    # 도달 정점이 이미 지난 정점이고
    # 만들어지는 간선이 새로운 간선이면 하나의 공간이 만들어진다
    while q:
        nx, ny = q.popleft()

        if vertex[(nx, ny)] == 1:
            if edge[(x, y, nx, ny)] == 0:
                answer += 1

        vertex[(nx, ny)] = 1
        edge[(x, y, nx, ny)] = 1
        edge[(nx, ny, x, y)] = 1

        x, y = nx, ny
    return answer

print(solution([6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]))