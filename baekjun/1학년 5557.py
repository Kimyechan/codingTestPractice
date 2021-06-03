n = int(input())
numbers = list(map(int, input().split()))

dp = [[0] * (20 + 1) for _ in range(n - 1)]

dp[0][numbers[0]] = 1
for i in range(1, n - 1):
    for j in range(20 + 1):
        if dp[i - 1][j] != 0:
            if j - numbers[i] >= 0:
                dp[i][j - numbers[i]] += dp[i - 1][j]
            if j + numbers[i] <= 20:
                dp[i][j + numbers[i]] += dp[i - 1][j]

print(dp[n - 2][numbers[n - 1]])