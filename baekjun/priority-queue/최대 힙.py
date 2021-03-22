import heapq
import sys

n = int(input())

queue = []
for _ in range(n):
    x = int(sys.stdin.readline())

    if x == 0:
        if len(queue) == 0:
            print(0)
        else:
            value = heapq.heappop(queue)
            print(value * -1)
    else:
        heapq.heappush(queue, x * -1)
