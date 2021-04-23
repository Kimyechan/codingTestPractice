# check
def checkImpossible(answer):
    for x, y, a in answer:
        if a == 0:
            if y != 0 and (x, y - 1, 0) not in answer and (x - 1, y, 1) not in answer \
                    and (x, y, 1) not in answer:
                return True
        else:
            if (x, y - 1, 0) not in answer and (x + 1, y - 1, 0) not in answer \
                    and not ((x - 1, y, 1) in answer and (x + 1, y, 1) in answer):
                return True
    return False


def solution(n, build_frame):
    answer = set()

    for frame in build_frame:
        x, y, a, b = frame
        if b == 1:
            answer.add((x, y, a))
            if checkImpossible(answer):
                answer.remove((x, y, a))
        else:
            answer.remove((x, y, a))
            if checkImpossible(answer):
                answer.add((x, y, a))

    answer = list(map(list, answer))
    answer.sort(key=lambda x: (x[0], x[1], x[2]))
    return answer