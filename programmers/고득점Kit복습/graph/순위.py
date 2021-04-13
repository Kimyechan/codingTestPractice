# check
# from collections import defaultdict
#
#
# def solution(n, results):
#     answer = 0
#     graphWin = defaultdict(set)
#     graphLose = defaultdict(set)
#
#     for result in results:
#         graphLose[result[0]].add(result[1])
#         graphWin[result[1]].add(result[0])
#
#     for i in range(1, n + 1):
#         for loser in graphLose[i]:
#             graphWin[loser] |= graphWin[i]
#         for winner in graphWin[i]:
#             graphLose[winner] |= graphLose[i]
#
#     for i in range(1, n + 1):
#         if len(graphLose[i]) + len(graphWin[i]) == n - 1:
#             answer += 1
#
#     return answer
#
#
# print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))
from collections import defaultdict
from collections import deque


def solution(n, results):
    answer = 0
    wins = defaultdict(list) # i가 이긴 사람의 목록
    loses = defaultdict(list) # i가 패배한 사람의 목록

    for result in results:
        wins[result[0]].append(result[1])
        loses[result[1]].append(result[0])

    for i in range(1, n + 1):
        q = deque([i])
        visited = [False] * (n + 1)
        wCount = 0

        while q:
            v = q.popleft()
            visited[v] = True

            for nextP in wins[v]:
                if not visited[nextP]:
                    visited[nextP] = True
                    wCount += 1
                    q.append(nextP)

        q = deque([i])
        visited = [False] * (n + 1)
        lCount = 0

        while q:
            v = q.popleft()
            visited[v] = True

            for nextP in loses[v]:
                if not visited[nextP]:
                    visited[nextP] = True
                    lCount += 1
                    q.append(nextP)

        if wCount + lCount == n - 1:
            answer += 1

    return answer