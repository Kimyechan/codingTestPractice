def solution(brown, yellow):
    answer = []
    total = brown + yellow
    for i in range(3, total + 1):
        if total % i != 0:
            continue
        a = i
        b = total // i
        if (a - 2) * (b - 2) == yellow:
            answer = [a, b]
            break

    answer.sort(reverse=True)

    return answer


print(solution(10 , 2))
print(solution(8, 1))
print(solution(24, 24))
