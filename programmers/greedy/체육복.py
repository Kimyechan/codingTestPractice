def solution(n, lost, reserve):
    answer = 0
    wHave = [1] * n

    for x in lost:
        wHave[x - 1] -= 1

    for o in reserve:
        wHave[o - 1] += 1

    for idx, w in enumerate(wHave):
        if w == 2:
            if idx != 0 and wHave[idx - 1] == 0:
                wHave[idx - 1] = 1
                wHave[idx] -= 1
            elif idx != n - 1 and wHave[idx + 1] == 0:
                wHave[idx + 1] = 1
                wHave[idx] -= 1

    for have in wHave:
        if have != 0:
            answer += 1

    return answer