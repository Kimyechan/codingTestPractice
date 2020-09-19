def solution(citations):
    answer = 0

    for num in range(10001):
        lower = 0
        higher = 0
        for citation in citations:
            if num > citation:
                lower += 1
            else:
                higher += 1
        if higher >= num >=lower:
            answer = max(answer, num)

    return answer


print(solution([3, 0, 6, 1, 5]))
