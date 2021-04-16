# check
# n, k = map(int, input().split())
#
# dp = [list([0] * (n + 1)) for _ in range(k + 1)]
#
# for i in range(n + 1):
#     dp[1][i] = 1
#
# for i in range(1, k + 1):
#     dp[i][0] = 1
#
# for i in range(2, k + 1):
#     for j in range(1, n + 1):
#         dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 1000000000
#
# print(dp[k][n])

n, k = map(int, input().split())

dp = [list([0] * (n + 1)) for _ in range(k + 1)]

for i in range(1, k + 1):
    dp[i][0] = 1

for i in range(0, n + 1):
    dp[1][i] = 1

for i in range(2, k + 1):
    for j in range(1, n + 1):
        dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 1000000000

print(dp[k][n])
