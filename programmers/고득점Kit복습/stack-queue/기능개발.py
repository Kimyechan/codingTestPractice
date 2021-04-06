import math


def solution(progresses, speeds):
    answer = []
    days = []
    for i in range(len(progresses)):
        days.append(math.ceil((100 - progresses[i]) / speeds[i]))

    stack = []
    for day in days:
        if len(stack) == 0:
            stack.append(day)
        else:
            count = 0
            while len(stack) != 0 and stack[-1] < day and stack[0] < day:
                stack.pop()
                count += 1

            stack.append(day)

            if count != 0:
                answer.append(count)

    answer.append(len(stack))
    return answer


print(solution([93, 30, 55], [1, 30, 5]))
