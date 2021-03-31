import sys
n, m = map(int, input().split())

parents = [i for i in range(n + 1)]
ranks = [0 for i in range(n + 1)]


def find(a):
    if parents[a] != a:
        parents[a] = find(parents[a])
    return parents[a]


def unionByRank(a, b):
    parent1 = find(a)
    parent2 = find(b)

    if ranks[parent1] > ranks[parent2]:
        parents[parent2] = parent1
    else:
        parents[parent1] = parent2
        if ranks[parent1] == ranks[parent2]:
            ranks[parent2] += 1


for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    unionByRank(a, b)

for i in range(1, n + 1):
    find(i)

print(len(set(parents[1:])))