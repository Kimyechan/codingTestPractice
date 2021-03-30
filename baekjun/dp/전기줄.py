n = int(input())

line = []
for _ in range(n):
    line.append(list(map(int, input().split())))

line.sort()

dp = [1] * n
for i in range(n):
    for j in range(i):
        if line[i][1] > line[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))