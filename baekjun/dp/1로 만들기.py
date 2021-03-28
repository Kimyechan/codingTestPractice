n = int(input())

dp = []
if n < 3:
    dp = [n] * 4
else:
    dp = [n] * (n + 1)

dp[0] = 0
dp[1] = 0
dp[2] = 1
dp[3] = 1
for i in range(4, n + 1):
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    dp[i] = min(dp[i], dp[i - 1] + 1)

print(dp[n])

# dp = [n] * (n + 1)
#
#
# def count(x):
#     if x == 2:
#         return 1
#     elif x == 3:
#         return 1
#
#     if dp[x] != n:
#         return dp[x]
#
#     if x % 3 == 0:
#         dp[x] = min(dp[x], count(x // 3) + 1)
#     if x % 2 == 0:
#         dp[x] = min(dp[x], count(x // 2) + 1)
#
#     dp[x] = min(dp[x], count(x - 1) + 1)
#     return dp[x]
#
#
# print(count(n))