import sys

n = int(sys.stdin.readline())
spot = list(map(int, sys.stdin.readline().split()))

newSpot = set(spot)
newSpot = list(newSpot)
newSpot.sort()
compressSpot = dict()

newNum = 0
for num in newSpot:
    compressSpot[num] = newNum
    newNum += 1

for num in spot:
    print(compressSpot[num], end=" ")