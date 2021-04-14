# import math
#
#
# def solution(progresses, speeds):
#     answer = []
#     days = []
#     for i in range(len(progresses)):
#         days.append(math.ceil((100 - progresses[i]) / speeds[i]))
#
#     stack = []
#     for day in days:
#         if len(stack) == 0:
#             stack.append(day)
#         else:
#             count = 0
#             while len(stack) != 0 and stack[-1] < day and stack[0] < day:
#                 stack.pop()
#                 count += 1
#
#             stack.append(day)
#
#             if count != 0:
#                 answer.append(count)
#
#     answer.append(len(stack))
#     return answer
#
#
# print(solution([93, 30, 55], [1, 30, 5]))
import math


def solution(progresses, speeds):
    answer = []

    needDays = [math.ceil((100 - progresses[i]) / speeds[i]) for i in range(len(progresses))]
    stack = []
    for needDay in needDays:
        if len(stack) == 0:
            stack.append(needDay)
        else:
            deployCount = 0
            while len(stack) != 0 and stack[0] < needDay:
                stack.pop()
                deployCount += 1
            stack.append(needDay)
            if deployCount != 0:
                answer.append(deployCount)

    if len(stack) != 0:
        answer.append(len(stack))

    return answer


print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))























