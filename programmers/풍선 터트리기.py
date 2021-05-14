# check
# def solution(a):
#     answer = 0
#     minLeft = [float('inf')] * len(a)
#     minRight = [float('inf')] * len(a)
#
#     leftMinValue = float('inf')
#     for i in range(len(a)):
#         if leftMinValue > a[i]:
#             leftMinValue = a[i]
#         minLeft[i] = leftMinValue
#
#     rightMinValue = float('inf')
#     for i in range(len(a) - 1, -1, -1):
#         if rightMinValue > a[i]:
#             rightMinValue = a[i]
#         minRight[i] = rightMinValue
#
#     for i in range(len(a)):
#         if a[i] <= minLeft[i] or a[i] <= minRight[i]:
#             answer += 1
#
#     return answer


def solution(a):
    answer = 0
    minL = [0] * len(a)
    minR = [0] * len(a)

    minLV = float('inf')
    for i in range(len(a)):
        if minLV > a[i]:
            minLV = a[i]
        minL[i] = minLV

    minRV = float('inf')
    for i in range(len(a) - 1, -1, -1):
        if minRV > a[i]:
            minRV = a[i]
        minR[i] = minRV

    for i in range(len(a)):
        if minL[i] >= a[i] or minR[i] >= a[i]:
            answer += 1

    return answer

print(solution([9, -1, -5]))
