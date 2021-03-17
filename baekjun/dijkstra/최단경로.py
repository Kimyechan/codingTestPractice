from collections import defaultdict
import heapq

v, e = map(int, input().split())
start = int(input())

graph = defaultdict(list)
for _ in range(e):
    v1, v2, weight = map(int, input().split())
    graph[v1].append([v2, weight])


distances = {node: float('inf') for node in range(1, v + 1)}
distances[start] = 0
q = []
heapq.heappush(q, [distances[start], start])

while q:
    curDis, curNode = heapq.heappop(q)

    if distances[curNode] < curDis:
        continue

    for adj, weight in graph[curNode]:
        dis = curDis + weight

        if dis < distances[adj]:
            distances[adj] = dis
            heapq.heappush(q, [distances[adj], adj])

for i in range(1, v + 1):
    if distances[i] == float('inf'):
        print("INF")
    else:
        print(distances[i])