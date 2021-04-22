# check
import sys
from collections import defaultdict


n = int(input())
weight = [0] * (n + 1)
tree = defaultdict(list)
dp = [[0, 0] for _ in range(n + 1)]
visited = [False] * (n + 1)

weight[1:] = list(map(int, sys.stdin.readline().split()))

for _ in range(n - 1):
    n1, n2 = map(int, sys.stdin.readline().split())
    tree[n1].append(n2)
    tree[n2].append(n1)


def countDSet(node):
    visited[node] = True
    dp[node][0] = 0
    dp[node][1] = weight[node]

    for adj in tree[node]:
        if not visited[adj]:
            countDSet(adj)
            dp[node][0] += max(dp[adj][0], dp[adj][1])
            dp[node][1] += dp[adj][0]


traceResult = []
traceCheck = [False] * (n + 1)


def trace(current, prev):
    traceCheck[current] = True

    if prev == 1:
        for node in tree[current]:
            if not traceCheck[node]:
                trace(node, 0)
    else:
        if dp[current][0] < dp[current][1]:
            traceResult.append(current)
            for node in tree[current]:
                if not traceCheck[node]:
                    trace(node, 1)
        else:
            for node in tree[current]:
                if not traceCheck[node]:
                    trace(node, 0)


countDSet(1)
print(max(dp[1][0], dp[1][1]))

trace(1, 0)
traceResult.sort()
print(*traceResult)

# trace_result = []
# trace_check = [True for _ in range(n + 1)]
#
#
# def Trace(cur, pre):  # 현재노드와 이전노드가 포함되었는지 안되었는지 0:포함됨 1:포함안됨
#     trace_check[cur] = False
#
#     if pre == 0:  # 이전노드가 포함되었다면
#         for i in tree[cur]:  # 현재노드는 포함할수없음
#             if trace_check[i]:
#                 Trace(i, 1)
#     else:  # 이전노드가 포함되어있지않다면
#         if dp[cur][0] < dp[cur][1]:  # 현재노드를 포함한 부분이 더크다면
#             trace_result.append(cur)  # 현재노드 포함
#             for i in tree[cur]:
#                 if trace_check[i]:
#                     Trace(i, 0)
#         else:  # 현재노드를 포함하지 않은부분이 크다면
#             for i in tree[cur]:
#                 if trace_check[i]:
#                     Trace(i, 1)