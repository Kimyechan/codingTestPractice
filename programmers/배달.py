from collections import defaultdict
import heapq


def solution(N, road, K):
    answer = 0
    graph = defaultdict(list)
    for r in road:
        graph[r[0]].append((r[1], r[2]))
        graph[r[1]].append((r[0], r[2]))

    distances = [float('inf')] * (N + 1)
    distances[1] = 0

    q = [(0, 1)]
    heapq.heapify(q)

    while q:
        v = heapq.heappop(q)

        if v[0] > distances[v[1]]:
            continue

        for adj, weight in graph[v[1]]:
            dis = v[0] + weight
            if distances[adj] > dis:
                distances[adj] = dis
                heapq.heappush(q, (dis, adj))

    for dis in distances:
        if dis <= K:
            answer += 1

    return answer


print(solution(5, [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]], 3))

