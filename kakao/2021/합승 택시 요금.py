from collections import defaultdict
import heapq


def dijkstra(n, start, graph):
    distance = [float('inf')] * (n + 1)
    distance[start] = 0
    q = [(start, 0)]

    while q:
        currentNode, currentDis = heapq.heappop(q)

        for nextNode, weight in graph[currentNode]:
            if distance[nextNode] > currentDis + weight:
                distance[nextNode] = currentDis + weight
                heapq.heappush(q, (nextNode, distance[nextNode]))

    return distance


def solution(n, s, a, b, fares):
    graph = defaultdict(list)

    for fare in fares:
        graph[fare[0]].append([fare[1], fare[2]])
        graph[fare[1]].append([fare[0], fare[2]])

    answer = float('inf')
    distanceSToAny = dijkstra(n, s, graph)
    for i in range(1, n + 1):
        distanceIToEnd = dijkstra(n, i, graph)
        sToA = distanceSToAny[i] + distanceIToEnd[a]
        sToB = distanceSToAny[i] + distanceIToEnd[b]
        if answer > sToA + sToB - distanceSToAny[i]:
            answer = sToA + sToB - distanceSToAny[i]

    return answer


print(solution(6, 4, 6, 2,
               [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22],
                [1, 6, 25]]))

# 플로이드 와샬
# import heapq
#
# def solution(n, s, a, b, fares):
#     d = [ [ 20000001 for _ in range(n) ] for _ in range(n) ]
#     for x in range(n):
#         d[x][x] = 0
#     for x, y, c in fares:
#         d[x-1][y-1] = c
#         d[y-1][x-1] = c
#
#     for i in range(n):
#         for j in range(n):
#             for k in range(n):
#                 if d[j][k] > d[j][i] + d[i][k]:
#                     d[j][k] = d[j][i] + d[i][k]
#
#     minv = 40000002
#     for i in range(n):
#         minv = min(minv, d[s-1][i]+d[i][a-1]+d[i][b-1])
#     return minv