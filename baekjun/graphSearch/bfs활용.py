from collections import deque
from collections import defaultdict

dataList = [
    [0, 1],
    [2, 3],
    [3, 4],
    [3, 5]
]


def changeToGraph(dataList):
    graph = defaultdict(list)

    for data in dataList:
        graph[data[0]].append(data[1])
        graph[data[1]].append(data[0])

    return graph


graph = changeToGraph(dataList)
visited = [False] * len(graph.keys())


def countGraph():
    count = 0

    for node in graph.keys():
        if not visited[node]:
            bfs(node, graph)
            count += 1

    return count


def bfs(start, graph):
    q = deque([start])

    while q:
        v = q.popleft()
        if not visited[v]:
            visited[v] = True
            for e in graph[v]:
                if not visited[e]:
                    q.append(e)


print(countGraph())