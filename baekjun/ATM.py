n = int(input())
times = list(map(int, input().split()))

times.sort()

dp = [0] * n
dp[0] = times[0]
for i in range(1, n):
    dp[i] = dp[i - 1] + times[i]

print(sum(dp))