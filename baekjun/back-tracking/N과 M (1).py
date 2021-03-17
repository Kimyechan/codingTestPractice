n, m = map(int, input().split())
result = []


def backTracking(numMax, numberLen, numberList):
    if len(numberList) == numberLen:
        result.append(numberList[:])
        return

    for num in range(1, numMax + 1):
        if num not in numberList:
            numberList.append(num)
            backTracking(numMax, numberLen, numberList)
            numberList.pop()


backTracking(n, m, [])
for numbers in result:
    for num in numbers:
        print(num, end=" ")
    print()