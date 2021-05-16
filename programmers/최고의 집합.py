# check
def solution(n, s):
    answer = []
    if n > s:
        return [-1]

    div = s // n
    mod = s % n

    answer = [div] * n
    for i in range(n - 1, n - 1 - mod, -1):
        answer[i] += 1

    return answer