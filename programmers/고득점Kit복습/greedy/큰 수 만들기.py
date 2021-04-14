# check check
# def solution(number, k):
#     stack = []
#     for i, num in enumerate(number):
#         while len(stack) > 0 and stack[-1] < num and k > 0:
#             stack.pop()
#             k -= 1
#
#         if k == 0:
#             stack.append(number[i:])
#             break
#
#         stack.append(num)
#
#     if k > 0:
#         stack = number[:-k]
#     return "".join(stack)


def solution(number, k):
    stack = []
    for num in number:
        while len(stack) != 0 and stack[-1] < num and k != 0:
            stack.pop()
            k -= 1

        stack.append(num)

    if k != 0:
        answer = stack[:-k]
    else:
        answer = stack

    result = ""
    for i in answer:
        result += str(i)

    return result


# print(solution("1924", 2))
print(solution("1231234", 3))
print(solution("4177252841", 4))




















