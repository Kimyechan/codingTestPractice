# check
T = int(input())

for _ in range(T):
    n = int(input())
    coins = map(int, input().split())
    m = int(input())

    dp = [0] * (m + 1)
    for coin in coins:
        for x in range(coin, m + 1):
            if x == coin:
                dp[x] = dp[x] + 1
            else:
                dp[x] = dp[x] + dp[x - coin]

    print(dp[-1])