# check
# import sys
# from collections import defaultdict
#
# t = int(input())
# n = int(input())
# listA = list(map(int, sys.stdin.readline().split()))
# m = int(input())
# listB = list(map(int, sys.stdin.readline().split()))
#
# nSumDict = defaultdict(int)
#
# for i in range(n):
#     for j in range(i, n):
#         nSumDict[sum(listA[i:j + 1])] += 1
#
# result = 0
# for i in range(m):
#     for j in range(i, m):
#         mSum = sum(listB[i:j+1])
#         if nSumDict[t - mSum] != 0:
#             result += nSumDict[t - mSum]

# 누적합, 이분탐색 사용
# import sys
# import bisect
#
#
# def cal_sum_list(array, size):
#     array_sum_list = list()
#
#     for s_size in range(1, size + 1):
#         temp_sum = sum(array[0:s_size])
#         array_sum_list.append(temp_sum)
#         for s_crd in range(s_size, size):
#             temp_sum += array[s_crd]
#             temp_sum -= array[s_crd - s_size]
#             array_sum_list.append(temp_sum)
#
#     return sorted(array_sum_list), set(array_sum_list)
#
#
# if __name__ == "__main__":
#     t = int(sys.stdin.readline())
#     len_a = int(sys.stdin.readline())
#     a = list(map(int, sys.stdin.readline().replace('\r', '').split()))
#     len_b = int(sys.stdin.readline())
#     b = list(map(int, sys.stdin.readline().replace('\r', '').split()))
#
#     a_sum_list, set_a = cal_sum_list(a, len_a)
#     b_sum_list, set_b = cal_sum_list(b, len_b)
#
#     count = 0
# 타겟 값 마지막 인덱스 - 타겟 값 시작 인덱스
#     for i in a_sum_list:
#         target = t - i
#         count += bisect.bisect_right(b_sum_list, target) - bisect.bisect_left(b_sum_list, target)
#
#     print(count)


# import sys
# from collections import defaultdict
#
# t = int(input())
# n = int(input())
# listA = list(map(int, sys.stdin.readline().split()))
# m = int(input())
# listB = list(map(int, sys.stdin.readline().split()))
#
# nSumDict = defaultdict(int)
#
# for i in range(n):
#     sum = 0
#     for j in range(i, n):
#         sum += listA[j]
#         nSumDict[sum] += 1
#
# result = 0
# for i in range(m):
#     sum = 0
#     for j in range(i, m):
#         sum += listB[j]
#         if nSumDict[t - sum] != 0:
#             result += nSumDict[t - sum]
import sys

t = int(sys.stdin.readline())
n = int(sys.stdin.readline())
aList = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
bList = list(map(int, sys.stdin.readline().split()))

aSumList = []
for i in range(n):
    sum = 0
    for j in range(i, n):
        sum += aList[j]
        aSumList.append(sum)

bSumList = []
for i in range(m):
    sum = 0
    for j in range(i, m):
        sum += bList[j]
        bSumList.append(sum)

bSumList.sort()
result = 0
for aSum in aSumList:
    remainSum = t - aSum

    start = 0
    end = len(bSumList) - 1
    while start < end:
        mid = (start + end) // 2
        if bSumList[mid] >= remainSum:
            end = mid
        else:
            start = mid + 1
    startIndex = end

    start = 0
    end = len(bSumList) - 1
    while start < end:
        mid = (start + end) // 2
        if bSumList[mid] > remainSum:
            end = mid
        else:
            start = mid + 1
    endIndex = end

    if bSumList[endIndex] == remainSum:
        result += endIndex - startIndex + 1
    else:
        result += endIndex - startIndex

print(result)


# 7
# 4
# 1 3 1 2
# 3
# 1 3 2



















# print(result)
