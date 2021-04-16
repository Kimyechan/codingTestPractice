# check
# from itertools import combinations
# import sys
#
# n = int(input())
#
# board = [list(map(int, input().split())) for i in range(n)]
# visited = [list([False] * n) for _ in range(n)]
#
# sumResults = []
# for i in range(1, n - 1):
#     for j in range(1, n - 1):
#         sumResults.append([board[i - 1][j] + board[i][j] + board[i][j - 1] + board[i + 1][j] + board[i][j + 1], (i, j)])
#
# answer = sys.maxsize
# for combi in combinations(sumResults, 3):
#     spotSet = []
#     sumValue = 0
#     for candi in combi:
#         value, (i, j) = candi
#         spotSet.append((i, j))
#         spotSet.append((i - 1, j))
#         spotSet.append((i, j - 1))
#         spotSet.append((i + 1, j))
#         spotSet.append((i, j + 1))
#         sumValue += value
#
#     if len(set(spotSet)) != 15:
#         continue
#     else:
#         answer = min(answer, sumValue)
#
# print(answer)
import sys

n = int(input())

board = [list(map(int, input().split())) for _ in range(n)]
result = sys.maxsize
moves = [(0, 0), (0, -1), (0, 1), (-1, 0), (1, 0)]


def calcCost(i, j, k):
    sumValue = 0
    locationList = []

    for start in [i, j, k]:
        x = start // n
        y = start % n
        for move in moves:
            nx = x + move[0]
            ny = y + move[1]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                return sys.maxsize
            else:
                sumValue += board[nx][ny]
                locationList.append((nx, ny))
    if len(set(locationList)) == 15:
        return sumValue
    else:
        return sys.maxsize


for i in range(n * n):
    for j in range(i + 1, n * n):
        for k in range(j + 1, n * n):
            result = min(result, calcCost(i, j, k))

print(result)













