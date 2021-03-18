import math
from itertools import combinations
import sys
t = int(input())

for _ in range(t):
    n = int(input())
    v = []
    totalV = [0, 0]
    for _ in range(n):
        x, y = map(int, input().split())
        totalV[0] += x
        totalV[1] += y
        v.append([x, y])

    candidate = list(combinations(v, n // 2))
    result = sys.maxsize
    for endV in candidate[:len(candidate) // 2]:
        sumV = [0, 0]
        for e in endV:
            sumV[0] += e[0]
            sumV[1] += e[1]

        removeX = totalV[0] - sumV[0]
        removeY = totalV[1] - sumV[1]

        sumV[0] -= removeX
        sumV[1] -= removeY

        result = min(result, math.sqrt(sumV[0] ** 2 + sumV[1] ** 2))

    print('%.12f' % result)

# n = int(input())
# v = []
# for _ in range(n):
#     x, y = map(int, input().split())
#     v.append([x, y])
#
# endV = combinations(v, n // 2)
# result = sys.maxsize
# for endV in combinations(v, n // 2):
#     startV = deepcopy(v)
#     sumV = [0, 0]
#     for e in endV:
#         sumV[0] += e[0]
#         sumV[1] += e[1]
#         startV.remove(e)
#
#     for s in startV:
#         sumV[0] -= s[0]
#         sumV[1] -= s[1]
#
#     result = min(result, math.sqrt(sumV[0] ** 2 + sumV[1] ** 2))
#
# print(result)
