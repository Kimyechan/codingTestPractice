# check
from functools import cmp_to_key


def compare(a, b):
    ab = a + b
    ba = b + a
    return int(ba) - int(ab)


def solution(numbers):
    answer = ''
    numbersStr = [str(num) for num in numbers]
    numbersStr.sort(key=cmp_to_key(compare))

    for numStr in numbersStr:
        answer += numStr

    result = 0
    for value in answer:
        result += int(value)

    if result == 0:
        return "0"
    return answer


print(solution([6, 10, 2]))
print(solution([0, 0, 0, 0, 0]))
