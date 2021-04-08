from itertools import permutations
import math


def solution(numbers):
    answer = 0

    perm = []
    for i in range(1, len(numbers) + 1):
        for temp in permutations(numbers, i):
            num = ""
            for value in temp:
                num += value
            perm.append(int(num))

    perm = list(set(perm))
    for value in perm:
        if value == 0:
            continue
        if value == 1:
            continue
        if value == 2:
            answer += 1
            continue

        flag = 0
        for i in range(2, int(math.sqrt(value)) + 1):
            if value % i == 0:
                flag = 1
                break
        if flag == 0:
            answer += 1

    return answer


# print(solution("17"))
print(solution("011"))
