def solution(number, k):
    stack = []
    for i, num in enumerate(number):
        while len(stack) > 0 and stack[-1] < num and k > 0:
            stack.pop()
            k -= 1

        if k == 0:
            stack.append(number[i:])
            break

        stack.append(num)

    if k > 0:
        stack = number[:-k]
    return "".join(stack)




























# def solution(number, k):
#     stack = []
#
#     for i, num in enumerate(number):
#         while len(stack) > 0 and stack[-1] < num and k > 0:
#             stack.pop()
#             k -= 1
#
#         if k == 0:
#             stack += number[i:]
#             break
#
#         stack.append(num)
#
#     if k > 0:
#         stack = stack[:-k]
#
#     answer = "".join(stack)
#     return answer
