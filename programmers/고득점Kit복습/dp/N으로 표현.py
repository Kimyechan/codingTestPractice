# check
def solution(N, number):
    answer = 0
    if number == N:
        return 1

    count = [[] for i in range(9)]
    for i in range(1, 9):
        count[i].append(int(str(N) * i))

    for i in range(2, 9):
        for j in range(1, i):
            for a in count[j]:
                for b in count[i - j]:
                    count[i].append(a + b)
                    count[i].append(a - b)
                    count[i].append(a * b)
                    if b != 0:
                        count[i].append(a // b)

        if number in count[i]:
            answer = i
            break

    if answer == 0:
        answer = -1

    return answer


print(solution(5, 12))
print(solution(2, 11))