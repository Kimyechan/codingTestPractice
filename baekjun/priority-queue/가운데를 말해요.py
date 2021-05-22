# check
# import heapq
# import sys
#
# n = int(input())
# left = []
# right = []
#
# for _ in range(n):
#     num = int(sys.stdin.readline())
#
#     if len(left) == len(right):
#         heapq.heappush(left, (-num, num))
#     else:
#         heapq.heappush(right, (num, num))
#
#     if right and left[0][1] > right[0][1]:
#         leftMax = heapq.heappop(left)[1]
#         rightMin = heapq.heappop(right)[1]
#         heapq.heappush(left, (-rightMin, rightMin))
#         heapq.heappush(right, (leftMax, leftMax))
#
#     print(left[0][1])

import sys
import heapq

n = int(sys.stdin.readline())
left = []
right = []

for i in range(n):
    num = int(sys.stdin.readline())

    if len(left) == len(right):
        heapq.heappush(left, (-num, num))
    else:
        heapq.heappush(right, (num, num))

    if right and left[0][1] > right[0][1]:
        leftMax = heapq.heappop(left)[1]
        rightMin = heapq.heappop(right)[1]
        heapq.heappush(left, (-rightMin, rightMin))
        heapq.heappush(right, (leftMax, leftMax))

    print(left[0][1])

























