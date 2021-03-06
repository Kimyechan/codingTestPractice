import sys

count = int(sys.stdin.readline())

numList = list()

for _ in range(count):
    numList.append(int(sys.stdin.readline()))
numList.sort()


def averageValue(data):
    return round(sum(data) / count)


def centerValue(data):
    minIndex = count // 2
    return data[minIndex]


def mostValue(data):
    frequency = dict()

    for x in data:
        if x in frequency.keys():
            frequency[x] = frequency.get(x) + 1
        else:
            frequency[x] = 1

    maxF = 0
    maxFValues = list()
    for value, f in frequency.items():
        if maxF < f:
            maxFValues.clear()
            maxFValues.append(value)
            maxF = f
        elif maxF == f:
            maxFValues.append(value)

    if len(maxFValues) == 1:
        return maxFValues[0]
    else:
        return maxFValues[1]


def maxMinusMin(data):
    return max(data) - min(data)


print(averageValue(numList))
print(centerValue(numList))
print(mostValue(numList))
print(maxMinusMin(numList))