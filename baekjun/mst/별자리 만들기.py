import math
import heapq

n = int(input())
stars = [list(map(float, input().split())) for _ in range(n)]

edges = []

parent = [0] * n
rank = [0] * n

for i in range(n):
    parent[i] = i


def calcDistance(star1, star2):
    return math.sqrt((star1[0] - star2[0]) ** 2 + (star1[1] - star2[1]) ** 2)


def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]


def unionByRank(n1, n2):
    p1 = find(n1)
    p2 = find(n2)

    if rank[p1] > rank[p2]:
        parent[p2] = p1
    else:
        parent[p1] = p2
        if rank[p1] == rank[p2]:
            rank[p2] += 1


for i in range(len(stars)):
    for j in range(i + 1, len(stars)):
        edges.append([calcDistance(stars[i], stars[j]), i, j])

heapq.heapify(edges)
totalDis = 0

while edges:
    edge = heapq.heappop(edges)

    if find(edge[1]) != find(edge[2]):
        unionByRank(edge[1], edge[2])
        totalDis += edge[0]

print(format(totalDis, ".2f"))