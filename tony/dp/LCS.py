# check
numbers1 = input()
numbers2 = input()

dp = [list([0] * (len(numbers2) + 1)) for _ in range(len(numbers1) + 1)]

for i in range(1, len(numbers1) + 1):
    for j in range(1, len(numbers2) + 1):
        if numbers1[i - 1] != numbers2[j - 1]:
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
        else:
            dp[i][j] = dp[i - 1][j - 1] + 1

print(dp[len(numbers1)][len(numbers2)])