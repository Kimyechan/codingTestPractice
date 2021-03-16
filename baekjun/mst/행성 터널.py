import heapq

N = int(input())
planet = []
for i in range(N):
    x, y, z = map(int, input().split())
    planet.append([x, y, z, i])

edges = []
for i in range(3):
    planet.sort(key=lambda l: l[i])
    for j in range(N - 1):
        edges.append([abs(planet[j + 1][i] - planet[j][i]), planet[j][3], planet[j+1][3]])

heapq.heapify(edges)
connectedP = set()
totalCost = 0

parent = [0] * N
rank = [0] * N

for i in range(N):
    parent[i] = i


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


while edges:
    edge = heapq.heappop(edges)

    # if len(connectedP) == N: # 노드 갯수 체크하는 부분 넣으면 실패함 이유는 모르겠음..
    #     break

    if find(edge[1]) != find(edge[2]):
        unionByRank(edge[1], edge[2])
        totalCost += edge[0]
        # connectedP.add(edge[1])
        # connectedP.add(edge[2])

print(totalCost)

# N = int(input())
# planet = []
# for i in range(N):
#     x, y, z = map(int, input().split())
#     planet.append([x, y, z, i])
#
# edges = []
# for i in range(3):
#     planet.sort(key=lambda l: l[i])
#     for j in range(N - 1):
#         edges.append([abs(planet[j + 1][i] - planet[j][i]), planet[j][3], planet[j+1][3]])
#
# edges.sort()
# totalCost = 0
#
# parent = [0] * N
# rank = [0] * N
#
# for i in range(N):
#     parent[i] = i
#
#
# def find(node):
#     if parent[node] != node:
#         parent[node] = find(parent[node])
#     return parent[node]
#
#
# def unionByRank(n1, n2):
#     p1 = find(n1)
#     p2 = find(n2)
#
#     if rank[p1] > rank[p2]:
#         parent[p2] = p1
#     else:
#         parent[p1] = p2
#         if rank[p1] == rank[p2]:
#             rank[p2] += 1
#
#
# for edge in edges:
#     if find(edge[1]) != find(edge[2]):
#         unionByRank(edge[1], edge[2])
#         totalCost += edge[0]
#
# print(totalCost)