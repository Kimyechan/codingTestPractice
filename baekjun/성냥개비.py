# t = int(input())
# count = dict()
# count[1] = 2
# count[2] = 5
# count[3] = 5
# count[4] = 5
# count[4] = 4
# count[5] = 5
# count[6] = 6
# count[7] = 3
# count[8] = 7
# count[9] = 6
# count[0] = 6
#
# result = []
#
#
# def searchMinMax(n, count, combi):
#     if n < 0:
#         return
#
#     if n == 0 and combi[0] != "0":
#         result.append(int(combi))
#         return
#
#     for i in range(10):
#         n -= count[i]
#         searchMinMax(n, count, combi + str(i))
#         n += count[i]
#
#
# for _ in range(t):
#     n = int(input())
#
#     result = []
#     searchMinMax(n, count, "")
#
#     print(min(result), end=" ")
#     print(max(result))

from collections import defaultdict

t = int(input())


def getMax(num):
    maxNum = ""
    if num % 2 == 0:
        maxNum += "1"
    else:
        maxNum += "7"
    length = num // 2

    for i in range(length - 1):
        maxNum += "1"

    return maxNum


def getMin(num):
    minNums = defaultdict(int)
    minNums[2] = 1
    minNums[3] = 7
    minNums[4] = 4
    minNums[5] = 2
    minNums[6] = 6
    minNums[7] = 8
    minNums[8] = 10

    addNums = ["1", "7", "4", "2", "0", "8"]

    for i in range(9, num + 1):
        for j in range(2, 8):
            curr = str(minNums[i - j]) + addNums[j - 2]
            if minNums[i] == 0:
                minNums[i] = int(curr)
            else:
                minNums[i] = min(minNums[i], int(curr))

    return minNums[num]


for _ in range(t):
    n = int(input())

    maxValue = getMax(n)
    minValue = getMin(n)

    print(minValue, end=" ")
    print(maxValue)