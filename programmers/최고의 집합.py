# check
# def solution(n, s):
#     answer = []
#     if n > s:
#         return [-1]
#
#     div = s // n
#     mod = s % n
#
#     answer = [div] * n
#     for i in range(n - 1, n - 1 - mod, -1):
#         answer[i] += 1
#
#     return answer


# def solution(n, k):
#     answer = []
#
#     numbers = [i for i in range(1, n + 1)]
#     factorial = []
#     num = 1
#     for i in range(1, n):
#         num *= i
#         factorial.append(num)
#
#     for i in range(1, n):
#         idx = (k - 1) // factorial[n - i - 1]
#         k = k % factorial[n - i - 1]
#         answer.append(numbers.pop(idx))
#
#     answer.append(numbers[0])
#     return answer


def solution(n, s):
    answer = []
    div = s // n
    mod = s % n

    if div == 0:
        return [-1]

    answer = [div] * n
    for i in range(n - 1, n - mod - 1, - 1):
        answer[i] += 1

    return answer