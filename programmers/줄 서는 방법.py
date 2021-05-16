# check
def solution(n, k):
    answer = []
    numbers = [i for i in range(1, n + 1)]

    values = []
    value = 1
    for i in range(1, n):
        value *= i
        values.append(value)

    for i in range(n - 2, -1, -1):
        idx = (k - 1) // values[i]
        k = k % values[i]
        answer.append(numbers[idx])
        numbers.pop(idx)

    answer.append(numbers[0])
    return answer

# from math import factorial
#
#
# def solution(n, k):
#     answer = []
#     nl = list(range(1, n + 1))
#
#     while n != 0:
#         fact = factorial(n - 1)
#         answer.append(nl.pop((k - 1) // fact))
#         n -= 1
#         k %= fact
#
#     return answer


print(solution(3, 5))