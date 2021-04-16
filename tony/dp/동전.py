# check check
# T = int(input())
#
# for _ in range(T):
#     n = int(input())
#     coins = map(int, input().split())
#     m = int(input())
#
#     dp = [0] * (m + 1)
#     for coin in coins:
#         for x in range(coin, m + 1):
#             if x == coin:
#                 dp[x] = dp[x] + 1
#             else:
#                 dp[x] = dp[x] + dp[x - coin]
#
#     print(dp[-1])

t = int(input())

for _ in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    money = int(input())

    dp = [0] * (money + 1)

    for coin in coins:
        for i in range(coin, money + 1):
            if coin == i:
                dp[i] = dp[i] + 1
            else:
                dp[i] = dp[i] + dp[i - coin]

    print(dp[-1])





















