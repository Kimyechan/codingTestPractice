import sys

n = int(input())

g = [0]
for _ in range(n):
    g.append(int(sys.stdin.readline()))

dp = [0] * (n + 1)

dp[1] = g[1]

if n == 1:
    print(dp[1])
elif n == 2:
    print(g[1] + g[2])
else:
    for i in range(2, n + 1):
        dp[i] = max(g[i] + g[i - 1] + dp[i - 3], g[i] + g[i - 1] + dp[i - 4],  g[i] + dp[i - 2])

    print(max(dp[n], dp[n - 1]))