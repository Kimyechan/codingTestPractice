import heapq
import sys

t = int(input())


for _ in range(t):
    k = int(input())

    maxQ = []
    minQ = []

    count = 0
    countDict = dict()
    for _ in range(k):
        command, num = sys.stdin.readline().split()
        num = int(num)

        if command == 'I':
            if num in countDict:
                countDict[num] += 1
            else:
                countDict[num] = 1
            heapq.heappush(maxQ, (-num, num))
            heapq.heappush(minQ, (num, num))
        elif command == 'D':
            if num == 1:
                while maxQ:
                    maxTemp = heapq.heappop(maxQ)
                    if maxTemp[1] in countDict and countDict[maxTemp[1]] != 0:
                        countDict[maxTemp[1]] -= 1
                        if countDict[maxTemp[1]] == 0:
                            del countDict[maxTemp[1]]
                        break
            else:
                while minQ:
                    minTemp = heapq.heappop(minQ)
                    if minTemp[1] in countDict and countDict[minTemp[1]] != 0:
                        countDict[minTemp[1]] -= 1
                        if countDict[minTemp[1]] == 0:
                            del countDict[minTemp[1]]
                        break

    if not countDict:
        print("EMPTY")
    else:
        result = sorted(list(countDict.keys()))
        print("%d %d" % (result[-1], result[0]))
