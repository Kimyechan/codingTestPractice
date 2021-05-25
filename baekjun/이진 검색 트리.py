# check
import sys
sys.setrecursionlimit(10 ** 9)


def postOrder(start, end):
    if start > end:
        return
    div = end + 1
    for i in range(start + 1, end + 1):
        if preOrderList[i] > preOrderList[start]:
            div = i
            break

    postOrder(start + 1, div - 1)
    postOrder(div, end)
    print(preOrderList[start])


preOrderList = []
while True:
    try:
        preOrderList.append(int(sys.stdin.readline()))
    except:
        break

postOrder(0, len(preOrderList) - 1)

