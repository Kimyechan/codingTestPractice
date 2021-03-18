sList = [input() for _ in range(3)]

dp = [list([0] * (len(sList[2]) + 1) for _ in range(len(sList[1]) + 1)) for _ in range(len(sList[0]) + 1)]

for i in range(1, len(sList[0]) + 1):
    for j in range(1, len(sList[1]) + 1):
        for k in range(1, len(sList[2]) + 1):
            if sList[0][i-1] == sList[1][j-1] == sList[2][k-1]:
                dp[i][j][k] = dp[i-1][j-1][k-1] + 1
            else:
                dp[i][j][k] = max(dp[i-1][j][k],  dp[i][j-1][k], dp[i][j][k-1])

print(dp[len(sList[0])][len(sList[1])][len(sList[2])])
