t = int(input())

for _ in range(t):
    n = int(input())

    if n <= 3:
        dp = [0] * 4
    else:
        dp = [0] * (n + 1)

    dp[1] = 1
    dp[2] = 1
    dp[3] = 1

    if n == 1:
        print(1)
    elif n == 2:
        print(1)
    elif n == 3:
        print(1)
    else:
        for i in range(4, n + 1):
            dp[i] = dp[i - 2] + dp[i - 3]
        print(dp[n])