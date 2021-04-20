def solution(n, a, b):
    round = 1
    if a > b:
        a, b = b, a

    while a // 2 + 1 != b // 2 or b - 1 != a:
        if a % 2 == 0:
            a = a // 2
        else:
            a = a // 2 + 1

        if b % 2 == 0:
            b = b // 2
        else:
            b = b // 2 + 1

        round += 1

    return round


print(solution(8, 4, 7))


# def solution(n,a,b):
#     answer = 0
#     while a != b:
#         answer += 1
#         a, b = (a+1)//2, (b+1)//2
#
#     return answer
