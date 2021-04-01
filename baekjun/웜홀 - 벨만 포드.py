# from collections import defaultdict
# import sys
#
# tc = int(sys.stdin.readline())
# for _ in range(tc):
#     n, m, w = map(int, sys.stdin.readline().split())
#     graph = defaultdict(list)
#     dis = [1e9] * (n + 1)
#     dis[1] = 0
#
#     for _ in range(m):
#         n1, n2, weight = map(int, sys.stdin.readline().split())
#         graph[n1].append((n2, weight))
#         graph[n2].append((n1, weight))
#
#     for _ in range(w):
#         n1, n2, weight = map(int, sys.stdin.readline().split())
#         graph[n1].append((n2, -weight))
#
#     for _ in range(n-1):
#         for node in range(1, n + 1):
#             for adj, weight in graph[node]:
#                 # if dis[node] == float('inf'):
#                 #     continue
#                 if dis[adj] > dis[node] + weight:
#                     dis[adj] = dis[node] + weight
#
#     isTimeBack = False
#     for node in range(1, n + 1):
#         for adj, weight in graph[node]:
#             # if dis[node] == float('inf'):
#             #     continue
#             if dis[adj] > dis[node] + weight:
#                 isTimeBack = True
#                 break
#
#     if isTimeBack:
#         print("YES")
#     else:
#         print("NO")

from collections import defaultdict
import sys

tc = int(sys.stdin.readline())
for _ in range(tc):
    n, m, w = map(int, sys.stdin.readline().split())
    graph = defaultdict(list)
    dis = [int(1e9)] * (n + 1)
    dis[1] = 0

    for _ in range(m):
        n1, n2, weight = map(int, sys.stdin.readline().split())
        graph[n1].append((n2, weight))
        graph[n2].append((n1, weight))

    for _ in range(w):
        n1, n2, weight = map(int, sys.stdin.readline().split())
        graph[n1].append((n2, -weight))

    isTimeBack = False
    for count in range(1, n + 1):
        for node in range(1, n + 1):
            for adj, weight in graph[node]:
                if dis[adj] > dis[node] + weight:
                    dis[adj] = dis[node] + weight
                    if count == n:
                        isTimeBack = True

    if isTimeBack:
        print("YES")
    else:
        print("NO")