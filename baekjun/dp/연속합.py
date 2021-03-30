import sys
n = int(sys.stdin.readline())

numbers = list(map(int, sys.stdin.readline().split()))

result = -1000
dp = [0] * n
dp[0] = numbers[0]

for i in range(0, n):
    if i == 0:
        dp[i] = numbers[i]
    else:
        dp[i] = max(dp[i - 1] + numbers[i], numbers[i])
    result = max(result, dp[i])

print(result)