# from collections import defaultdict
# import heapq
#
#
# def solution(n, edge):
#     answer = 0
#
#     graph = defaultdict(list)
#     for e in edge:
#         graph[e[0]].append(e[1])
#         graph[e[1]].append(e[0])
#
#     distance = [float('inf')] * (n + 1)
#     distance[1] = 0
#     hq = [(1, 0)]
#     heapq.heapify(hq)
#
#     while hq:
#         current = heapq.heappop(hq)
#
#         if current[1] > distance[current[0]]:
#             continue
#
#         for nextNode in graph[current[0]]:
#             dis = current[1] + 1
#
#             if distance[nextNode] > dis:
#                 distance[nextNode] = dis
#                 heapq.heappush(hq, (nextNode, dis))
#
#     distance[0] = 0
#
#     maxDis = max(distance)
#     for d in distance:
#         if maxDis == d:
#             answer += 1
#
#     return answer
#
#
# print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
from collections import deque


def solution(n, edge):
    answer = 0

    graph = [[] for _ in range(n + 1)]

    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])

    distance = [-1] * (n + 1)
    distance[1] = 0

    q = deque([1])

    while q:
        currentNode = q.popleft()

        for nextNode in graph[currentNode]:
            if distance[nextNode] == -1:
                distance[nextNode] = distance[currentNode] + 1
                q.append(nextNode)

    maxDistance = max(distance)
    for d in distance:
        if d == maxDistance:
            answer += 1

    return answer

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))