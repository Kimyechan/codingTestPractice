from collections import defaultdict


def solution(n, words):
    answer = []

    useCheck = defaultdict(int)
    stack = []
    personNum = 1
    failFlag = False
    for i in range(len(words)):
        if len(stack) == 0:
            stack.append(words[i])
            useCheck[words[i]] = 1
        else:
            if stack[-1][-1] == words[i][0] and useCheck[words[i]] == 0:
                stack.append(words[i])
                useCheck[words[i]] = 1
            else:
                failFlag = True
                break
        personNum += 1

    a = personNum % n if personNum % n != 0 else n
    b = personNum // n if personNum % n == 0 else personNum // n + 1

    if not failFlag:
        answer = [0, 0]
    else:
        answer = [a, b]

    return answer