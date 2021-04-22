# check
# import sys
#
# sys.setrecursionlimit(10 ** 9)
#
# N, R, Q = map(int, sys.stdin.readline().split())
# Tree = [[] for _ in range(N + 1)]  # 트리 구성
# node_count = [0] * (N + 1)  # 노드 개수
# check = [True for _ in range(N + 1)]  # 방문여부
#
# for _ in range(N - 1):
#     U, V = map(int, sys.stdin.readline().split())
#     Tree[U].append(V)
#     Tree[V].append(U)
#
#
# def count_node(r):
#     node_count[r] = 1
#     for node in Tree[r]:  # 연결된 노드 탐색
#         if not node_count[node]:  # 방문가능하면
#             count_node(node)
#             node_count[r] += node_count[node]
#     return
#
#
# count_node(R)
#
# for _ in range(Q):
#     q = int(sys.stdin.readline())
#     print(node_count[q])
import sys
from collections import defaultdict
sys.setrecursionlimit(1000000)

N, R, Q = map(int, input().split())

tree = defaultdict(list)
for i in range(N - 1):
    n1, n2 = map(int, sys.stdin.readline().split())
    tree[n1].append(n2)
    tree[n2].append(n1)

nodeCount = [0] * (N + 1)


def countNodeEachRoot(r):
    nodeCount[r] = 1
    for adj in tree[r]:
        if nodeCount[adj] == 0:
            countNodeEachRoot(adj)
            nodeCount[r] += nodeCount[adj]
    return


countNodeEachRoot(R)

for _ in range(Q):
    root = int(sys.stdin.readline())
    print(nodeCount[root])
# import sys
#
# sys.setrecursionlimit(10 ** 6)
# input = sys.stdin.readline
# N, R, Q = map(int, input().split())
# adjList = [[] for _ in range(N)]
# for i in range(N - 1):
#     u, v = map(int, input().split())
#     adjList[u - 1].append(v - 1)
#     adjList[v - 1].append(u - 1)
# visited = [False] * N
# cache = [1] * N
#
#
# def dfsDP(x):
#     visited[x] = True
#     for y in adjList[x]:
#         if visited[y]: continue
#         cache[x] += dfsDP(y)
#     return cache[x]
#
# dfsDP(R - 1)
# for _ in range(Q):
#     print(cache[int(input()) - 1])
