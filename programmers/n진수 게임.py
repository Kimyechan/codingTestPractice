def changeNum(maxNum, n):
    result = ""

    for i in range(maxNum):
        num = i
        resultTemp = ""
        charNumList = ["A", "B", "C", "D", "E", "F"]
        while num // n != 0:
            if num % n - 10 >= 0:
                resultTemp += charNumList[num % n - 10]
            else:
                resultTemp += str(num % n)
            num //= n
        if num % n - 10 >= 0:
            resultTemp += charNumList[num % n - 10]
        else:
            resultTemp += str(num % n)
        result += resultTemp[::-1]

    return result


def solution(n, t, m, p):
    answer = ''
    maxNum = t * m
    numSeq = changeNum(maxNum, n)

    for i in range(t):
        answer += numSeq[(p - 1) + m * i]

    return answer
