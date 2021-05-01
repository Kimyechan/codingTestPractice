# check
# import sys
#
# sys.setrecursionlimit(10 ** 9)
#
#
# def dfs(node, a, visited, graph):
#     global answer
#     visited[node] = True
#     now = a[node]
#
#     for adj in graph[node]:
#         if not visited[adj]:
#             now += dfs(adj, a, visited, graph)
#
#     answer += abs(now)
#
#     return now
#
#
# def solution(a, edges):
#     global answer
#     answer = 0
#     graph = [[] for _ in range(len(a) + 1)]
#     visited = [False] * len(a)
#
#     for edge in edges:
#         graph[edge[0]].append(edge[1])
#         graph[edge[1]].append(edge[0])
#
#     result = dfs(0, a, visited, graph)
#
#     if result != 0:
#         answer = -1
#
#     return answer

from collections import defaultdict
import sys

sys.setrecursionlimit(10 ** 9)


def dfs(node, a, graph, visited):
    global answer
    visited[node] = True

    for adj in graph[node]:
        if not visited[adj]:
            a[node] += dfs(adj, a, graph, visited)

    answer += abs(a[node])

    return a[node]


def solution(a, edges):
    global answer
    answer = 0
    graph = defaultdict(list)
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    visited = [False] * len(a)
    dfs(0, a, graph, visited)

    if a[0] != 0:
        answer = -1

    return answer