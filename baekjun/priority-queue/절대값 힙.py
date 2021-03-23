import heapq
import sys

n = int(input())

q = []
for _ in range(n):
    x = int(sys.stdin.readline())

    if x == 0:
        if len(q) == 0:
            print(0)
        else:
            value = heapq.heappop(q)
            print(value[1])
    else:
        heapq.heappush(q, (abs(x), x))