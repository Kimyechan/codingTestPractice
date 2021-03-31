# import sys
# sys.setrecursionlimit(1000000)
#
# a, b, c = map(int, input().split())
#
# dp = [-1] * (b + 1)
#
#
# def calcPow(a, b, c):
#     if b == 1:
#         return a
#     if b == 0:
#         return 1
#
#     bLeft = b - b // 2
#     leftResult = 0
#     if dp[bLeft] == -1:
#         leftResult = calcPow(a, bLeft, c)
#         dp[bLeft] = leftResult
#     else:
#         leftResult = dp[bLeft]
#
#     bRight = b // 2
#     rightResult = 0
#     if dp[bRight] == -1:
#         rightResult = calcPow(a, bRight, c)
#         dp[bRight] = rightResult
#     else:
#         rightResult = dp[bRight]
#
#     return (leftResult * rightResult) % c
#
#
# print(calcPow(a, b, c))

import sys
sys.setrecursionlimit(1000000)

a, b, c = map(int, input().split())


def calcPow(a, b, c):
    if b == 1:
        return a % c
    if b == 0:
        return 1

    if b % 2 == 0:
        return ((calcPow(a, b // 2, c) % c) ** 2) % c
    else:
        return ((((calcPow(a, b // 2, c) % c) ** 2) % c) * a) % c


print(calcPow(a, b, c))