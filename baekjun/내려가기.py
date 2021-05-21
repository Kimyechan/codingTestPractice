# import sys
#
# n = int(sys.stdin.readline())
# dp = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
#
# maxDp = dp[0]
# for i in range(1, n):
#     dp1 = dp[i][0] + max(maxDp[0], maxDp[1])
#     dp2 = dp[i][1] + max(maxDp[0], maxDp[1], maxDp[2])
#     dp3 = dp[i][2] + max(maxDp[1], maxDp[2])
#     maxDp = [dp1, dp2, dp3]
#
# maxResult = max(maxDp)
#
# minDp = dp[0]
# for i in range(1, n):
#     dp1 = dp[i][0] + min(minDp[0], minDp[1])
#     dp2 = dp[i][1] + min(minDp[0], minDp[1], minDp[2])
#     dp3 = dp[i][2] + min(minDp[1], minDp[2])
#     minDp = [dp1, dp2, dp3]
#
# minResult = min(minDp)
#
# print(maxResult, end=" ")
# print(minResult)

# immutable mutable -> 공간 복잡도, list -> mutable, 변수 -> immutable
import sys

n = int(sys.stdin.readline())

temp = list(map(int, sys.stdin.readline().split()))
maxDp = temp[:]
minDp = temp[:]
for i in range(1, n):
    temp1 = list(map(int, sys.stdin.readline().split()))
    temp2 = temp1[:]

    temp1[0] += max(maxDp[0], maxDp[1])
    temp1[1] += max(maxDp[0], maxDp[1], maxDp[2])
    temp1[2] += max(maxDp[1], maxDp[2])
    maxDp = temp1

    temp2[0] += min(minDp[0], minDp[1])
    temp2[1] += min(minDp[0], minDp[1], minDp[2])
    temp2[2] += min(minDp[1], minDp[2])
    minDp = temp2

maxResult = max(maxDp)
minResult = min(minDp)

print(maxResult, end=" ")
print(minResult)