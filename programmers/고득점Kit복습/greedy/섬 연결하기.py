# kruskal
# def solution(n, costs):
#     parents = [i for i in range(n)]
#     ranks = [0] * n
#
#     def find(node):
#         if parents[node] != node:
#             parents[node] = find(parents[node])
#         return parents[node]
#
#     def unionByRak(n1, n2):
#         p1 = find(n1)
#         p2 = find(n2)
#
#         if ranks[p1] > ranks[p2]:
#             parents[p2] = p1
#         else:
#             parents[p1] = p2
#             if ranks[p1] == ranks[p2]:
#                 ranks[p2] += 1
#
#     costs.sort(key=lambda x: x[2])
#
#     answer = 0
#     for cost in costs:
#         if find(cost[0]) != find(cost[1]):
#             unionByRak(cost[0], cost[1])
#             answer += cost[2]
#
#     return answer

import heapq


def solution(n, costs):
    graph = [[] for i in range(n)]

    for cost in costs:
        graph[cost[0]].append([cost[2], cost[1]])
        graph[cost[1]].append([cost[2], cost[0]])

    q = graph[0]
    heapq.heapify(q)
    connectedNode = [0]
    answer = 0

    while q:
        weight, node = heapq.heappop(q)

        if node not in connectedNode:
            connectedNode.append(node)
            answer += weight

        for w, v in graph[node]:
            if v not in connectedNode:
                heapq.heappush(q, [w, v])

    return answer


print(solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]))
