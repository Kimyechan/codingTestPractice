# check
# sumNum = [0] * 102
# dp = [list([0] * 52) for _ in range(102)]
# visited = [list([False] * 52) for _ in range(102)]
#
#
# def areaSum(num, area):
#     if area == 0:
#         return 0
#     if num < 2 * area - 1:
#         return -987654321
#     if visited[num][area]:
#         return dp[num][area]
#
#     visited[num][area] = True
#     dp[num][area] = areaSum(num - 1, area)
#
#     for i in range(num, 0, -1):
#         dp[num][area] = max(dp[num][area], sumNum[num] - sumNum[i - 1] + areaSum(i - 2, area - 1))
#
#     return dp[num][area]
#
#
# if __name__ == "__main__":
#     n, m = map(int, input().split())
#
#     for i in range(1, n + 1):
#         num = int(input())
#         sumNum[i] = sumNum[i - 1] + num
#
#     result = areaSum(n, m)
#     print(result)
import sys


def dfs(n, m):
    if m == 0:
        return 0
    if n < 0:
        return -sys.maxsize
    if dp[n][m]:
        return dp[n][m]

    dp[n][m] = dfs(n-1, m)
    for i in range(n, 0, -1):
        dp[n][m] = max(dp[n][m], dfs(i-2, m-1) + (prefix_sum[n] - prefix_sum[i-1]))

    return dp[n][m]


n, m = map(int, input().split())
prefix_sum = [0]*(n+1)
for i in range(1, n+1):
    num = int(input())
    prefix_sum[i] = prefix_sum[i-1] + num
dp = [[0]*(m+1) for _ in range(n+1)]

print(dfs(n,m))