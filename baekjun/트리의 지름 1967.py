from collections import deque
from collections import defaultdict
import sys

n = int(input())
tree = defaultdict(list)

for _ in range(n - 1):
    n1, n2, weight = map(int, sys.stdin.readline().split())
    tree[n1].append((n2, weight))
    tree[n2].append((n1, weight))


def calcMaxVertex(start):
    visited = [False] * (n + 1)
    distance = [0] * (n + 1)
    maxLen = 0
    maxVertex = 0
    q = deque([(start, 0)])

    while q:
        v = q.popleft()
        visited[v[0]] = True

        for nextV in tree[v[0]]:
            if not visited[nextV[0]]:
                visited[nextV[0]] = True
                distance[nextV[0]] = nextV[1] + v[1]
                q.append((nextV[0], distance[nextV[0]]))
                if maxLen < distance[nextV[0]]:
                    maxLen = distance[nextV[0]]
                    maxVertex = nextV[0]

    return maxVertex, maxLen


result1 = calcMaxVertex(1)
result2 = calcMaxVertex(result1[0])

print(result2[1])