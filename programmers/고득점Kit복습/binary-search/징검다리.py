# check
# 최초로 n개 이상을 삭제한 값에서 -1


def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)
    start = 1
    end = distance

    while start < end:
        current = 0
        removeCount = 0
        mid = (start + end) // 2

        for rock in rocks:
            diff = rock - current
            if diff < mid:
                removeCount += 1
            else:
                current = rock

        if removeCount > n:
            end = mid
        else:
            start = mid + 1

    return end - 1


print(solution(25, [2, 14, 11, 21, 17], 2))