# check
import sys
from collections import defaultdict
sys.setrecursionlimit(100000000)

n = int(input())
tree = defaultdict(list)

for _ in range(n - 1):
    n1, n2 = map(int, sys.stdin.readline().split())
    tree[n1].append(n2)
    tree[n2].append(n1)

visited = [False] * (n + 1)
dp = [[0, 0] for _ in range(n + 1)]


def countEarlyAdaptor(node):
    visited[node] = True
    dp[node][0] = 0
    dp[node][1] = 1
    for adj in tree[node]:
        if not visited[adj]:
            countEarlyAdaptor(adj)
            dp[node][0] += dp[adj][1]
            dp[node][1] += min(dp[adj][0], dp[adj][1])


countEarlyAdaptor(1)
print(min(dp[1][0], dp[1][1]))