def solution(answers):
    result = [0, 0, 0]
    size = len(answers)
    re = size // 40
    pick1 = [1, 2, 3, 4, 5] * 8 * (re + 1)
    pick2 = [2, 1, 2, 3, 2, 4, 2, 5] * 5 * (re + 1)
    pick3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 4 * (re + 1)

    for idx, answer in enumerate(answers):
        if pick1[idx] == answer:
            result[0] += 1
        if pick2[idx] == answer:
            result[1] += 1
        if pick3[idx] == answer:
            result[2] += 1

    maxV = max(result)

    fResult = []
    for idx, value in enumerate(result):
        if value == maxV:
            fResult.append(idx + 1)

    fResult.sort()
    return fResult