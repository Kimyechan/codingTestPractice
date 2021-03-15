import sys
sys.setrecursionlimit(100000)

K, N = map(int, input().split())
lines = list()
for _ in range(K):
    lines.append(int(input()))

maxLine = max(lines)


def binarySearch(array, start, end):
    if start > end:
        return end

    midLength = (start + end) // 2

    count = 0
    for line in array:
        count += line // midLength

    if count >= N:
        return binarySearch(array, midLength+1, end)
    else:
        return binarySearch(array, start, midLength-1)


print(binarySearch(lines, 1, maxLine))

# # 다른 분 풀이
# from sys import stdin
#
# K, N = map(int,stdin.readline().split())
# li = list(map(int,stdin.readlines()))
# h, l = sum(li)//N, 1
#
# while l <= h :
#     mid = (h+l)//2
#     cnt = sum([x//mid for x in li])
#     if cnt < N:
#         h = mid - 1
#     elif cnt >= N:
#         l = mid + 1
#         ans = mid
# print(ans)