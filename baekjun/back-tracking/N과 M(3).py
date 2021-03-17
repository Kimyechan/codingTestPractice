N, M = map(int, input().split())


def backTracking(n, numberList, m):
    if len(numberList) == m:
        result.append(numberList[:])
        return

    for num in range(1, n + 1):
        numberList.append(num)
        backTracking(n, numberList, m)
        numberList.pop()


result = []
backTracking(N, [], M)

for numbers in result:
    for number in numbers:
        print(number, end=" ")
    print()
