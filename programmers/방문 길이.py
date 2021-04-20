from collections import defaultdict


def solution(dirs):
    answer = 0
    direction = dict()

    direction["U"] = (0, 1)
    direction["L"] = (-1, 0)
    direction["D"] = (0, -1)
    direction["R"] = (1, 0)

    path = defaultdict(int)
    current = (0, 0)
    for dir in dirs:
        arrow = direction[dir]
        next = (current[0] + arrow[0], current[1] + arrow[1])

        if next[0] > 5 or next[0] < -5 or next[1] > 5 or next[1] < -5:
            continue

        if path[(current, next)] == 0:
            answer += 1
            path[(current, next)] = 1
            path[(next, current)] = 1

        current = next

    return answer


print(solution("ULURRDLLU"))