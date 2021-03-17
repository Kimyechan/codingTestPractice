n, m = map(int, input().split())
commands = [list(map(int, input().split())) for _ in range(m)]

parent = [i for i in range(n + 1)]
rank = [0] * (n + 1)


def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]


def union(n1, n2):
    p1 = find(n1)
    p2 = find(n2)

    if rank[p1] > rank[p2]:
        parent[p2] = p1
    else:
        parent[p1] = p2
        if rank[p1] == rank[p2]:
            rank[p2] += 1


for c in commands:
    if c[0] == 0:
        union(c[1], c[2])
    else:
        if find(c[1]) != find(c[2]):
            print("NO")
        else:
            print("YES")