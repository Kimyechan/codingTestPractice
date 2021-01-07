import sys

sys.setrecursionlimit(100000)


def solution(p):
    answer = ''

    def makeCorrect(p):
        if p == "":
            return p
        countL, countR = 0, 0
        uLen = 0
        u = ""
        v = ""
        correct = 0
        for x in p:
            if x == "(":
                countL += 1
                u = u + "("
            else:
                countR += 1
                u = u + ")"
            uLen += 1
            if countL < countR:
                correct = 1
            if countL == countR:
                break

        v = p[uLen:]
        if correct == 0:
            return u + makeCorrect(v)
        else:
            result = "(" + makeCorrect(v) + ")"
            temp = list(u)
            temp = temp[1: len(temp) - 1]
            for i in range(len(temp)):
                if temp[i] == "(":
                    temp[i] = ")"
                else:
                    temp[i] = "("
            u = ""
            for x in temp:
                u += x
            return result + u

    answer = makeCorrect(p)
    return answer

print(solution("()))((()"))