from collections import defaultdict
import heapq
import sys


def dijkstra(start, n, graph):
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

    return distances


testCase = int(input())

for _ in range(testCase):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())

    graph = defaultdict(list)
    gToH = 0
    for i in range(m):
        v1, v2, weight = map(int, input().split())
        graph[v1].append([v2, weight])
        graph[v2].append([v1, weight])
        if (v1 == g and v2 == h) or (v2 == g and v1 == h):
            gToH = weight

    candidates = []
    for _ in range(t):
        temp = int(sys.stdin.readline())
        candidates.append(temp)
    candidates.sort()

    sToAny = dijkstra(s, n, graph)
    gToAny = dijkstra(g, n, graph)
    hToAny = dijkstra(h, n, graph)

    for candidate in candidates:
        if sToAny[g] == float('inf') or sToAny[h] == float('inf') or sToAny[candidate] == float('inf') or gToAny[candidate] == float('inf') and hToAny[candidate] == float('inf'):
            continue

        if sToAny[g] + gToH + hToAny[candidate] == sToAny[candidate] or sToAny[h] + gToH + gToAny[candidate] == sToAny[candidate]:
            print(candidate, end=" ")
    print()

# 최단 거리 중복 될 경우 때문에 안됨
# from collections import defaultdict
# import heapq
# import sys
#
#
# def dijkstra(start, n, graph):
#     distances = {node: float('inf') for node in range(1, n + 1)}
#     course = [start] * (n + 1)
#     distances[start] = 0
#     q = []
#     heapq.heappush(q, [distances[start], start])
#
#     while q:
#         curDis, curNode = heapq.heappop(q)
#
#         if distances[curNode] < curDis:
#             continue
#
#         for adj, weight in graph[curNode]:
#             dis = curDis + weight
#             if dis < distances[adj]:
#                 distances[adj] = dis
#                 heapq.heappush(q, [dis, adj])
#                 course[adj] = curNode
#
#     return course
#
#
# testCase = int(input())
#
# for _ in range(testCase):
#     n, m, t = map(int, input().split())
#     s, g, h = map(int, input().split())
#
#     graph = defaultdict(list)
#     for i in range(m):
#         v1, v2, weight = map(int, input().split())
#         graph[v1].append([v2, weight])
#         graph[v2].append([v1, weight])
#
#     candidates = []
#     for _ in range(t):
#         temp = int(sys.stdin.readline())
#         candidates.append(temp)
#
#     course = dijkstra(s, n, graph)
#
#     possibleCourses = []
#     for candidate in candidates:
#         end = candidate
#         while course[end] != end:
#             prev = course[end]
#             if prev in [g, h] and end in [g, h]:
#                 possibleCourses.append(candidate)
#                 break
#             end = prev
#
#     possibleCourses.sort()
#     for possibleCourse in possibleCourses:
#         print(possibleCourse, end=" ")


import heapq as hq

n_test = int(input())


def Dijistra(s):  # s를 기준으로 하는 다익스트라
    q = []
    dist = [float('inf') for i in range(n + 1)]
    dist[s] = 0
    hq.heappush(q, (0, s))

    while q:
        weight, vertice = hq.heappop(q)
        if dist[vertice] < weight:
            continue

        for w, ver in adj[vertice]:
            if dist[ver] > w + weight:  # 현재 거리가 더 짧은 경로라면
                dist[ver] = w + weight
                hq.heappush(q, (w + weight, ver))

    return dist  # 거리 리스트를 반환한다.


for i in range(n_test):
    n, m, T = map(int, input().split())  # n교차로 m은 도로  t 목적지 후보 갯
    adj = [[] for i in range(n + 1)]  # 1번부터 n번노드까지 사용
    s, g, h = map(int, input().split())
    de = []
    # s 시작점 g와 h 사이의 교차로 사이에 있는 도로를 지나갔다.
    # 목적지 후보중  g와 h를 경유하는 최단 경로
    # 최단경로가 g,h를 포함하는 목적지를 찾으면된다.
    # 최단경로가 여러개 있을 수 있다.

    for i in range(m):
        a, b, d = map(int, input().split())
        adj[a].append((d, b))
        adj[b].append((d, a))
        if (a == g and b == h) or (a == h and b == g):
            path_g_h = d
    for i in range(T):
        de.append(int(input()))

    dist_s = Dijistra(s)  # 시작점에서 모든 노드로의 거리
    dist_h = Dijistra(h)  # h에서 모든 노드로의 거리
    dist_g = Dijistra(g)  # g에서 모든 노드로의 거리

    path_s_g = dist_s[g]  # s에서 g로 가는 최단거리
    path_s_h = dist_s[h]  # s에서 h로 가는 최단거리

    answer = []
    for t in de:
        path_g_t = dist_g[t]  # g에서 t로 가는 최단거리
        path_h_t = dist_h[t]  # h에서 t로 가는 최단거리
        path_s_t = dist_s[t]  # s에서 t로 가는 최단거리

        if path_g_t == float('inf') or path_h_t == float('inf') or path_s_t == float('inf'):
            continue
            # 거리값들중 무한대 값이 있으면 연결이 안되있는 노드임으로 불가능

        path_s_g_h_t = path_s_g + path_g_h + path_h_t
        path_s_h_g_t = path_s_h + path_g_h + path_g_t

        if (path_s_g_h_t == path_s_t or path_s_h_g_t == path_s_t):
            answer.append(t)

    answer.sort()

    print(' '.join(map(str, answer)))