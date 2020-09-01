# def solution(N, number):
#     E = [0 for _ in range(number+1)]
#     h = 0
#     if N % 2 == 0:
#         h = N/2
#     else:
#         h = int(N/2) + 1
#
#     for i in range(1, h+1):
#         E[i] = 2 + i - 1
#
#     x = 1
#     for i in range(h+1, N-1):
#         E[i] = N - 1 - x
#         x += 1
#
#     E[N] = 1
#
#     oneDist = 3
#     isFirst = True
#     for num in range(N+1, number+1):
#         s = set(str(num))
#         if len(s) == 1 and s - {1} == {} and isFirst:
#             isFirst = False
#             E[num] = oneDist
#             oneDist += 1
#         elif len(s) == 1 and s - {1} == {} and isFirst == False:
#             E[num] = oneDist
#             oneDist += 1
#         else:
#             E[num] = E[num-5] + 1
#     answer = E[number]
#     return answer
def solution(N, number):
    arr = [set() for i in range(8)]

    for i, num in enumerate(arr, start=1):
        num.add(int(str(N) * i))

    for i in range(1, len(arr)):
        for j in range(i):
            for op1 in arr[j]:
                for op2 in arr[i - j - 1]:
                    arr[i].add(op1 + op2)
                    arr[i].add(op1 - op2)
                    arr[i].add(op1 * op2)
                    if op2 != 0:
                        arr[i].add(op1 // op2)
        if number in arr[i]:
            answer = i + 1
            break
    else:
        answer = -1

    return answer























