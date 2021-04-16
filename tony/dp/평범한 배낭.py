# check
# n, k = map(int, input().split())
# bags = []
#
# for _ in range(n):
#     bags.append(list(map(int, input().split())))
# bags.sort()
#
# dp = [list([0] * (k + 1)) for _ in range(n + 1)]
#
# for i in range(len(bags)):
#     for j in range(1, k + 1):
#         if j < bags[i][0]:
#             dp[i + 1][j] = dp[i][j]
#         else:
#             dp[i + 1][j] = max(dp[i][j], dp[i][j - bags[i][0]] + bags[i][1])
#
# print(dp[n][k])

# n, k = map(int, input().split())
# dp = [list([0] * (k + 1)) for _ in range(n + 1)]
#
# for i in range(1, n + 1):
#     weight, value = map(int, input().split())
#     for j in range(1, k + 1):
#         if j < weight:
#             dp[i][j] = dp[i - 1][j]
#         else:
#             dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + value)
#
# print(dp[n][k])

n, k = map(int, input().split())

dp = [list([0] * (k + 1)) for _ in range(n + 1)]

for i in range(1, n + 1):
    weight, value = map(int, input().split())
    for j in range(1, k + 1):
        if j < weight:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + value)

print(dp[n][k])















