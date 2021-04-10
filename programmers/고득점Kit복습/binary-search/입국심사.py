def solution(n, times):
    start = 1
    end = 1000000000 * len(times)

    while start < end:
        mid = (start + end) // 2

        passCount = 0
        for i in range(len(times)):
            passCount += mid // times[i]

        if passCount >= n:
            end = mid
        else:
            start = mid + 1

    return end


print(solution(6, [7, 10]))