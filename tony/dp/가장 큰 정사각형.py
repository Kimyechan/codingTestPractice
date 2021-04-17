# check
# n, m = map(int, input().split())
#
# square = [list([0] * (m + 1)) for _ in range(n + 1)]
# dp = [list([0] * (m + 1)) for _ in range(n + 1)]
#
# for i in range(1, n + 1):
#     temp = list(input())
#     square[i][1:] = list(map(int, temp))
#
# maxLen = 0
# for i in range(1, n + 1):
#     for j in range(1, m + 1):
#         if square[i][j] == 1:
#             dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
#             maxLen = max(maxLen, dp[i][j])
#
# print(maxLen ** 2)
n, m = map(int, input().split())
square = [list([0] * (m + 1)) for _ in range(n + 1)]
dp = [list([0] * (m + 1)) for _ in range(n + 1)]

for i in range(1, n + 1):
    square[i][1:] = list(map(int, list(input())))

result = 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if square[i][j] == 1:
            dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
            result = max(result, dp[i][j])

print(result ** 2)

















