t = int(input())

for _ in range(t):
    n = int(input())
    dp = list([0, 0] for _ in range(n + 1))
    if n == 0:
        print(str(1) + " " + str(0))
    elif n == 1:
        print(str(0) + " " + str(1))
    else:
        dp[0] = [1, 0]
        dp[1] = [0, 1]

        for i in range(2, n + 1):
            dp[i][0] = dp[i - 1][0] + dp[i - 2][0]
            dp[i][1] = dp[i - 1][1] + dp[i - 2][1]

        print(*dp[n])