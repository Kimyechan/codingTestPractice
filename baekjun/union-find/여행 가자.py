n = int(input())
m = int(input())

connects = [list(map(int, input().split())) for _ in range(n)]
plans = list(map(int, input().split()))

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


for i in range(len(connects)):
    for j in range(len(connects[i])):
        if connects[i][j] == 1:
            union(i + 1, j + 1)


check = set()

for plan in plans:
    check.add(parent[plan])

if len(check) == 1:
    print("YES")
else:
    print("NO")