# check
import sys

sys.setrecursionlimit(10 ** 9)


def dfs(node, a, visited, graph):
    global answer
    visited[node] = True
    now = a[node]

    for adj in graph[node]:
        if not visited[adj]:
            now += dfs(adj, a, visited, graph)

    answer += abs(now)

    return now


def solution(a, edges):
    global answer
    answer = 0
    graph = [[] for _ in range(len(a) + 1)]
    visited = [False] * len(a)

    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    result = dfs(0, a, visited, graph)

    if result != 0:
        answer = -1

    return answer