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
