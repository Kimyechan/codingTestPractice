def solution(priorities, location):
    answer = 0

    while True:
        flagMax = 0
        for i in range(1, len(priorities)):
            if priorities[0] < priorities[i]:
                flagMax = 1

        if flagMax == 1:
            x = priorities.pop(0)
            priorities.append(x)
            if location == 0:
                location = len(priorities) - 1
            else:
                location -= 1
        else:
            priorities.pop(0)
            answer += 1
            if location == 0:
                break
            else:
                location -= 1

    return answer