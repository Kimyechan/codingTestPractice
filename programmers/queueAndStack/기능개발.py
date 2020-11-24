import math
from collections import deque


def solution(progresses, speeds):
    answer = []
    needDay = deque([])
    for i in range(len(progresses)):
        needDay.append(math.ceil((100 - progresses[i]) / speeds[i]))

    while needDay:
        currentDay = needDay.popleft()
        count = 1
        for value in needDay:
            if currentDay >= value:
                count += 1
            else:
                break
        for _ in range(count - 1):
            needDay.popleft()
        answer.append(count)

    return answer


print(solution([93, 30, 55], [1, 30, 5]))