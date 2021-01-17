# 이진수 변환 함수 -> bin()
def createTwo(twoN):
    array = []
    while True:
        if twoN // 2 == 1:
            array.append(twoN % 2)
            array.append(1)
            break
        array.append(twoN % 2)
        twoN = twoN // 2

    return array


def solution(n):
    if n == 1:
        return 2

    array1 = createTwo(n)

    start = 0
    for i in range(len(array1)):
        if array1[i] == 1:
            start = i
            break

    result = n + 2 ** start
    array2 = createTwo(result)

    diff = sum(array1) - sum(array2)

    for i in range(diff):
        result += 2 ** i

    return result


print(solution(78))