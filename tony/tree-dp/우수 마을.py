import sys
from collections import defaultdict
sys.setrecursionlimit(10 ** 9)

n = int(sys.stdin.readline())
peoples = [0] * (n + 1)
peoples[1:] = list(map(int, sys.stdin.readline().split()))

tree = defaultdict(list)
for _ in range(n - 1):
    n1, n2 = map(int, sys.stdin.readline().split())
    tree[n1].append(n2)
    tree[n2].append(n1)

visited = [False] * (n + 1)
dp = [[0 , 0] for _ in range(n + 1)]


def countGoodPeople(node):
    visited[node] = True
    dp[node][0] = 0
    dp[node][1] = peoples[node]

    for adj in tree[node]:
        if not visited[adj]:
            countGoodPeople(adj)
            dp[node][0] += max(dp[adj][1], dp[adj][0])
            dp[node][1] += dp[adj][0]


countGoodPeople(1)
print(max(dp[1][0], dp[1][1]))