n = int(input())

if n == 1:
    print(9)
elif n == 2:
    print(17)
else:
    dp = [list([0] * (9 + 1)) for _ in range(n + 1)]

    for i in range(1, 10):
        dp[1][i] = 1

    dp[2][0] = 1
    dp[2][1] = 1
    dp[2][9] = 1
    for i in range(2, 9):
        dp[2][i] = 2

    for i in range(3, n + 1):
        for j in range(0, 9 + 1):
            if j == 0:
                dp[i][j] = dp[i - 1][j + 1]
            elif j == 9:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]

    print(sum(dp[n]) % 1000000000)
# 1 2 3 4 5 6 7 8 9 -> 9
# 0 2 1 3 2 4 3 5 4 6 5 7 6 8 7 9 8 -> 17
# 34 - 2 = 32
# 64 - 4 = 60
#