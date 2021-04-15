# check
# from collections import deque, defaultdict
#
#
# def solution(arrows):
#     arrows.append(4)
#     answer = 0
#
#     q = deque([])
#     visited = defaultdict(int)
#     visitedPath = defaultdict(int)
#
#     move = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
#
#     x, y = 0, 0
#     for arrow in arrows:
#         for _ in range(2):
#             x += move[arrow][0]
#             y += move[arrow][1]
#             q.append((x, y))
#
#     now = (0, 0)
#     visited[now] = 1
#
#     while q:
#         next = q.popleft()
#
#         if visited[next] == 1:
#             if visitedPath[(now, next)] == 0:
#                 answer += 1
#         else:
#             visited[next] = 1
#
#         visitedPath[(now, next)] = 1
#         visitedPath[(next, now)] = 1
#         now = next
#
#     return answer
#
#
# print(solution([6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]))
from collections import defaultdict


def solution(arrows):
    answer = 0
    direction = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

    routes = []
    x, y = 0, 0
    for arrow in arrows:
        for _ in range(2):
            x += direction[arrow][0]
            y += direction[arrow][1]
            routes.append((x, y))

    visitedNode = defaultdict(int)
    visitedPath = defaultdict(int)

    current = (0, 0)
    visitedNode[current] = 1
    for node in routes:
        if visitedNode[node] == 1 and visitedPath[current, node] != 1:
            answer += 1

        visitedNode[node] = 1
        visitedPath[current, node] = 1
        visitedPath[node, current] = 1
        current = node

    return answer


print(solution([6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0, 4]))























