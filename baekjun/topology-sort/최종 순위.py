# import sys
# from collections import deque
#
#
# def topological():
#     q = deque()
#     # 진입 차수가 0인 값 q에 삽입
#     for i in range(1, n + 1):
#         if indegree[i] == 0:
#             q.append(i)
#
#     # 위상 정렬
#     result = []
#     for i in range(1, n + 1):
#         if len(q) == 0:  # 사이클이 있는 경우(시작점을 찾지 못한다)
#             return "IMPOSSIBLE"
#         index = q.popleft()
#         result.append(index)
#         for j in range(1, n + 1):
#             if graph[index][j]:  # index와 연결되어 있다면
#                 indegree[j] -= 1  # 진입 차수 감소
#                 if indegree[j] == 0:
#                     q.append(j)
#                     # if len(q) >= 2:  # 결과가 2개 이상 가능한 경우(일관성이 없는 정보)
#                     #     return "?"
#
#     return " ".join(map(str, result))
#
#
# if __name__ == "__main__":
#     t = int(sys.stdin.readline())
#     for _ in range(t):
#         n = int(sys.stdin.readline())
#         rank = list(map(int, sys.stdin.readline().split()))  # 작년 순위
#         graph = [[False] * (n + 1) for _ in range(n + 1)]
#         m = int(sys.stdin.readline())  # 순위 변동 수
#
#         # 진입 차수
#         indegree = [0] * (n + 1)
#
#         # 자신보다 순위가 낮은값으로 연결 (1등 -> 2등 ... -> n등)
#         for i in range(n):
#             for j in range(i + 1, n):
#                 graph[rank[i]][rank[j]] = True
#                 indegree[rank[j]] += 1
#
#         # 순위 변동
#         for _ in range(m):
#             a, b = map(int, sys.stdin.readline().split())
#             if not graph[a][b]:
#                 graph[b][a] = False
#                 indegree[b] += 1
#                 graph[a][b] = True
#                 indegree[a] -= 1
#             else:
#                 graph[b][a] = True
#                 indegree[b] -= 1
#                 graph[a][b] = False
#                 indegree[a] += 1
#
#         # 출력
#         answer = topological()
#         print(answer)
from collections import defaultdict, deque
import sys

testCase = int(input())

for _ in range(testCase):
    n = int(input())
    t = list(map(int, input().split()))

    graph = defaultdict(list)
    inDegree = [0] * (n + 1)

    for i in range(len(t)):
        graph[t[i]] = t[i + 1:]
        inDegree[t[i]] = i

    m = int(input())
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())

        if a in graph[b]:
            graph[b].remove(a)
            graph[a].append(b)

            inDegree[b] += 1
            inDegree[a] -= 1
        else:
            graph[a].remove(b)
            graph[b].append(a)

            inDegree[a] += 1
            inDegree[b] -= 1

    q = deque([])
    for i in range(1, n + 1):
        if inDegree[i] == 0:
            q.append(i)

    ans = []
    while q:
        cur = q.popleft()
        ans.append(cur)

        for nextRank in graph[cur]:
            inDegree[nextRank] -= 1
            if inDegree[nextRank] == 0:
                q.append(nextRank)

    if len(ans) == n:
        print(*ans)
    else:
        print("IMPOSSIBLE")


























