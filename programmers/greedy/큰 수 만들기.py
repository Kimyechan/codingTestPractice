## 틀림!!
# def solution(number, k):
#     answer = ''
#
#     isRemove = [False] * len(number)
#     countR = 0
#
#     for i in range(len(number)):
#         for j in range(i, -1, -1):
#             if int(number[i]) > int(number[j]) and not isRemove[j]:
#                 isRemove[j] = True
#                 countR += 1
#             if countR == k:
#                 break
#
#     for i in range(len(number)):
#         if not isRemove[i]:
#             answer += number[i]
#
#     return answer


def solution(number, k):
    stack = []

    for i, num in enumerate(number):
        while len(stack) > 0 and stack[-1] < num and k > 0:
            stack.pop()
            k -= 1

        if k == 0:
            stack += number[i:]
            break

        stack.append(num)

    if k > 0:
        stack = stack[:-k]

    answer = "".join(stack)
    return answer


print(solution("4177252841", 4))
