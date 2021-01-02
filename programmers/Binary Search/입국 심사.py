def solution(n, times):
    answer = 0

    start = 1
    end = n * max(times)

    while start <= end:
        checkAll = 0
        mid = (start + end) // 2

        for time in times:
            checkPerOne = mid // time
            checkAll += checkPerOne
            if n <= checkAll:
                answer = mid
                end = mid - 1
                break

        if n > checkAll:
            start = mid + 1

    return answer

# print(solution(8, [7, 10, 11, 11, 12, 11, 11]))
print(solution(6, [7, 10]))