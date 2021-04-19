# check LIS
# n = int(input())
# child = []
# for _ in range(n):
#     child.append(int(input()))
#
# dp = [1] * n
#
# for i in range(1, n):
#     for j in range(i):
#         if child[i] > child[j]:
#             dp[i] = max(dp[i], dp[j] + 1)
#
# print(n - max(dp))

n = int(input())
children = []

for _ in range(n):
    children.append(int(input()))

dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if children[j] < children[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))

























