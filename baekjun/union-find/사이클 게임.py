n, m = map(int, input().split())
games = [list(map(int, input().split())) for _ in range(m)]

parent = [i for i in range(n)]
rank = [0] * n


def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]


def union(n1, n2):
    p1 = parent[n1]
    p2 = parent[n2]

    if rank[p1] > rank[p2]:
        parent[p2] = p1
    else:
        parent[p1] = p2
        if rank[p1] == rank[p2]:
            rank[p2] += 1


result = 0
for i in range(len(games)):
    g = games[i]
    if find(g[0]) != find(g[1]):
        union(g[0], g[1])
    else:
        result = i + 1
        break

print(result)