# def solution(n, times):
#     start = 1
#     end = 1000000000 * len(times)
#
#     while start < end:
#         mid = (start + end) // 2
#
#         passCount = 0
#         for i in range(len(times)):
#             passCount += mid // times[i]
#
#         if passCount >= n:
#             end = mid
#         else:
#             start = mid + 1
#
#     return end
#
#
# print(solution(6, [7, 10]))


def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)

    start = 1
    end = distance
    result = []

    while start < end:
        location = 0
        mid = (start + end) // 2
        removeCount = 0

        for rock in rocks:
            if location + mid > rock:
                removeCount += 1
            else:
                location = rock

        if removeCount >= n:
            end = mid
            if removeCount == n:
                result.append(end)
        else:
            start = mid + 1

    return end - 1


print(solution(25, [2, 14, 11, 21, 17],	2))






















