# check
import sys
import heapq

n, k = map(int, sys.stdin.readline().split())
jews = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
bags = [int(sys.stdin.readline()) for _ in range(k)]

heapq.heapify(jews)
bags.sort()

possibleWeight = []
result = 0
for bag in bags:
    while jews and bag >= jews[0][0]:
        heapq.heappush(possibleWeight, -heapq.heappop(jews)[1])
    if possibleWeight:
        result += -heapq.heappop(possibleWeight)

print(result)