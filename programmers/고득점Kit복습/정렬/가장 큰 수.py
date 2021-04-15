# check
# from functools import cmp_to_key
#
#
# def compare(a, b):
#     ab = a + b
#     ba = b + a
#     return int(ba) - int(ab)
#
#
# def solution(numbers):
#     answer = ''
#     numbersStr = [str(num) for num in numbers]
#     numbersStr.sort(key=cmp_to_key(compare))
#
#     for numStr in numbersStr:
#         answer += numStr
#
#     result = 0
#     for value in answer:
#         result += int(value)
#
#     if result == 0:
#         return "0"
#     return answer
#
#
# print(solution([6, 10, 2]))
# print(solution([0, 0, 0, 0, 0]))
from functools import cmp_to_key


def compare(a, b):
    ab = int(str(a) + str(b))
    ba = int(str(b) + str(a))

    if ab > ba:
        return -1
    else:
        return 1


def solution(numbers):
    answer = ''
    numbers.sort(key=cmp_to_key(compare))

    for number in numbers:
        answer += str(number)

    return str(int(answer))


print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))





















