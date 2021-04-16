# check
# import sys
#
# n, m = map(int, input().split())
#
# peopleCount = [list([0] * (m + 1)) for _ in range(n + 1)]
# for i in range(1, n + 1):
#     temp = map(int, input().split())
#     peopleCount[i][1:] = temp
#
# countAdd = [list([0] * (m + 1)) for _ in range(n + 1)]
# countAdd[1][1] = peopleCount[1][1]
#
# for i in range(1, n + 1):
#     for j in range(1, m + 1):
#         countAdd[i][j] = peopleCount[i][j] + countAdd[i - 1][j] + countAdd[i][j - 1] - countAdd[i - 1][j - 1]
#
# k = int(input())
# for _ in range(k):
#     x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
#
#     result = countAdd[x2][y2] - countAdd[x2][y1 - 1] - countAdd[x1 - 1][y2] + countAdd[x1 - 1][y1 - 1]
#
#     print(result)
import sys


n, m = map(int, input().split())

land = [list([0] * (m + 1)) for _ in range(n + 1)]

for i in range(1, n + 1):
    temp = list(map(int, input().split()))
    land[i][1:] = temp

dp = [list([0] * (m + 1)) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = land[i][j] + dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]

k = int(input())
for _ in range(k):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    result = dp[x2][y2] - dp[x1 - 1][y2] - dp[x2][y1 - 1] + dp[x1 - 1][y1 - 1]
    print(result)
