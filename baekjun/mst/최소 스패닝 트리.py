# 프림
# from collections import defaultdict
# import heapq
#
# V, E = map(int, input().split())
# edgeList = [list(map(int, input().split())) for _ in range(E)]
#
# graph = defaultdict(list)
#
# for n1, n2, weight in edgeList:
#     graph[n1].append([weight, n1, n2])
#     graph[n2].append([weight, n2, n1])
#
#
# def prim(start):
#     q = graph[start]
#     heapq.heapify(q)
#     connected = [start]
#     totalWeight = 0
#
#     while q:
#         edge = heapq.heappop(q)
#         if edge[2] not in connected:
#             totalWeight += edge[0]
#             connected.append(edge[2])
#
#         for weight, n1, n2 in graph[edge[2]]:
#             if n2 not in connected:
#                 heapq.heappush(q, [weight, n1, n2])
#
#     return totalWeight
#
#
# print(prim(1))

# 크루스칼
import heapq

V, E = map(int, input().split())
temp = [list(map(int, input().split())) for _ in range(E)]
parent = [0] * (V + 1)
rank = [0] * (V + 1)

for v in range(V + 1):
    parent[v] = v


def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]


def unionByRank(n1, n2, rank):
    parent1 = find(n1)
    parent2 = find(n2)

    if rank[parent1] < rank[parent2]:
        parent[parent1] = parent2
    else:
        parent[parent2] = parent1
        if rank[parent1] == rank[parent2]:
            rank[parent1] += 1


def kruskal(edges):
    edgeList = []
    for n1, n2, weight in edges:
        edgeList.append([weight, n1, n2])

    heapq.heapify(edgeList)
    totalWeight = 0

    while edgeList:
        edge = heapq.heappop(edgeList)

        if find(edge[1]) != find(edge[2]):
            unionByRank(edge[1], edge[2], rank)
            totalWeight += edge[0]

    return totalWeight


print(kruskal(temp))









