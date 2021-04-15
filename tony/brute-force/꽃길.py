# check
from itertools import combinations
import sys

n = int(input())

board = [list(map(int, input().split())) for i in range(n)]
visited = [list([False] * n) for _ in range(n)]

sumResults = []
for i in range(1, n - 1):
    for j in range(1, n - 1):
        sumResults.append([board[i - 1][j] + board[i][j] + board[i][j - 1] + board[i + 1][j] + board[i][j + 1], (i, j)])

answer = sys.maxsize
for combi in combinations(sumResults, 3):
    spotSet = []
    sumValue = 0
    for candi in combi:
        value, (i, j) = candi
        spotSet.append((i, j))
        spotSet.append((i - 1, j))
        spotSet.append((i, j - 1))
        spotSet.append((i + 1, j))
        spotSet.append((i, j + 1))
        sumValue += value

    if len(set(spotSet)) != 15:
        continue
    else:
        answer = min(answer, sumValue)

print(answer)


















