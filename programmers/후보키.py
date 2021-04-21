from itertools import combinations


def solution(relation):
    keys = []
    columnLen = len(relation[0])

    columnList = [i for i in range(columnLen)]

    for i in range(1, columnLen + 1):
        for combi in combinations(columnList, i):
            isMini = True
            for key in keys:
                countEqual = 0
                for attr in key:
                    if attr in combi:
                        countEqual += 1
                if countEqual == len(key):
                    isMini = False
                    break

            if not isMini:
                continue

            keySetCheck = set()
            for r in relation:
                keyTemp = ""
                for col in combi:
                    keyTemp += str(r[col])
                keySetCheck.add(keyTemp)

            if len(keySetCheck) == len(relation):
                keys.append(list(combi))

    return len(keys)


print(solution([["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"],
                ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]))
