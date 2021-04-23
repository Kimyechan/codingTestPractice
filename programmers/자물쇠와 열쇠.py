from copy import deepcopy


def rotateKey(key):
    n = len(key)
    newKey = [list([0] * n) for _ in range(n)]

    for i in range(n):
        temp = []
        for j in range(n - 1, -1, -1):
            temp.append(key[j][i])
        newKey[i] = temp
    return newKey


def makeLocation(n):
    location = []
    for i in range(n):
        for j in range(n):
            location.append((i, j))
    return location


def solution(key, lock):
    answer = False
    n = len(key)
    m = len(lock)

    keyLocation = makeLocation(n)
    lockLocation = makeLocation(m)

    for _ in range(4):
        key = rotateKey(key)
        for m1 in range(-m + 1, m):
            for m2 in range(-m + 1, m):
                keyLocationSet = set([(kl[0] + m1, kl[1] + m2) for kl in keyLocation])
                lockLocationSet = set(lockLocation)
                sameList = list(lockLocationSet & keyLocationSet)
                lockTemp = deepcopy(lock)
                for s in sameList:
                    lockTemp[s[0]][s[1]] = lockTemp[s[0]][s[1]] ^ key[s[0] - m1][s[1] - m2]

                countCorrect = 0
                for i in range(m):
                    for j in range(m):
                        if lockTemp[i][j] == 1:
                            countCorrect += 1

                if countCorrect == m ** 2:
                    answer = True

    return answer


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
