def solution(s):
    zeroCount, loopCount = 0, 0

    while s != "1":
        array = []
        for x in s:
            array.append(int(x))
        zeroCount += len(array) - sum(array)
        s = bin(sum(array))[2:]
        loopCount += 1

    return [loopCount, zeroCount]