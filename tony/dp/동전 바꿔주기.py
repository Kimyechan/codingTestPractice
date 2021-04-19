# check check
# t = int(input())
# k = int(input())
#
# coins = []
# for _ in range(k):
#     coins.append(list(map(int, input().split())))
#
# dp = [list([0] * (t + 1)) for _ in range(k + 1)]
# dp[0][0] = 1
#
# coins.sort()
# sumMax = 0
# for i in range(1, k + 1):
#     for j in range(t + 1):
#         dp[i][j] = dp[i - 1][j]
#     for j in range(1, coins[i - 1][1] + 1):
#         for z in range(j * coins[i - 1][0], t + 1):
#             dp[i][z] += dp[i - 1][z - j * coins[i - 1][0]]
#
# print(dp[k][t])

t = int(input())
k = int(input())

coins = []

for _ in range(k):
    coins.append(list(map(int, input().split())))

dp = [list([0] * (t + 1)) for _ in range(k + 1)]
dp[0][0] = 1

for i in range(1, k + 1):
    for j in range(0, t + 1):
        dp[i][j] = dp[i - 1][j]
    for z in range(1, coins[i - 1][1] + 1):
        for w in range(z * coins[i - 1][0], t + 1):
            dp[i][w] += dp[i - 1][w - z * coins[i - 1][0]]

print(dp[k][t])
















































