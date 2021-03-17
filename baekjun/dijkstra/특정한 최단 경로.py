from collections import defaultdict
import heapq

n, e = map(int, input().split())
graph = defaultdict(list)
for i in range(e):
    v1, v2, weight = map(int, input().split())
    graph[v1].append([v2, weight])
    graph[v2].append([v1, weight])

needV1, needV2 = map(int, input().split())


def dijkstra(start, end, graph):
    distances = {node: float('inf') for node in range(1, n + 1)}
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
                heapq.heappush(q, [dis, adj])

    return distances[end]


case1 = dijkstra(1, needV1, graph) + dijkstra(needV1, needV2, graph) + dijkstra(needV2, n, graph) # 중복 제거 가능
case2 = dijkstra(1, needV2, graph) + dijkstra(needV2, needV1, graph) + dijkstra(needV1, n, graph)

if case1 == float('inf') or case2 == float('inf'):
    print(-1)
else:
    if case1 < case2:
        print(case1)
    else:
        print(case2)
