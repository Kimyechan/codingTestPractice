import sys
sys.setrecursionlimit(1000000)

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

zeroSquare = 0
oneSquare = 0


def cutPaper(paper, row, col, length):
    global zeroSquare
    global oneSquare

    zeroCount = 0
    oneCount = 0
    for i in range(row, row + length):
        for j in range(col, col + length):
            if paper[i][j] == 0:
                zeroCount += 1
            else:
                oneCount += 1

    if length == 0:
        return

    if zeroCount == length ** 2:
        zeroSquare += 1
        return
    elif oneCount == length ** 2:
        oneSquare += 1
        return

    cutPaper(paper, row, col, length // 2)
    cutPaper(paper, row + length // 2, col, length // 2)
    cutPaper(paper, row, col + length // 2, length // 2)
    cutPaper(paper, row + length // 2, col + length // 2, length // 2)


cutPaper(paper, 0, 0, n)

print(zeroSquare)
print(oneSquare)
