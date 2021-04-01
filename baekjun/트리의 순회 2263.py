# import sys
# sys.setrecursionlimit(1000000)
#
# n = int(input())
# inOrder = list(map(int, input().split()))
# postOrder = list(map(int, input().split()))
#
# index = [0] * (n + 1)
#
# for i in range(n):
#     index[inOrder[i]] = i
#
# preOrderResult = []
#
#
# def preOrder(inOrderStart, inOrderLast, postOrderStart, postOrderLast):
#     if inOrderStart > inOrderLast or postOrderStart > postOrderLast:
#         return
#
#     root = postOrder[postOrderLast]
#     preOrderResult.append(root)
#     left = index[root] - inOrderStart
#     # right = inOrderLast - index[root]
#
#     preOrder(inOrderStart, index[root] - 1, postOrderStart, postOrderStart + left - 1)
#     preOrder(index[root] + 1, inOrderLast, postOrderStart + left, postOrderLast - 1)
#     # preOrder(index[root] + 1, inOrderLast, postOrderLast - right, postOrderLast - 1)
#
#
# preOrder(0, n - 1, 0, n - 1)
# print(*preOrderResult)

import sys
sys.setrecursionlimit(1000000)

n = int(input())
inOrder = list(map(int, input().split()))
postOrder = list(map(int, input().split()))

index = [0] * (n + 1)

for i in range(n):
    index[inOrder[i]] = i

preOrderResult = []


def preOrder(inOrderStart, inOrderLast, postOrderStart, postOrderLast):
    if inOrderStart > inOrderLast or postOrderStart > postOrderLast:
        return

    root = postOrder[postOrderLast]
    preOrderResult.append(root)
    left = index[root] - inOrderStart

    preOrder(inOrderStart, index[root] - 1, postOrderStart, postOrderStart + left - 1)
    preOrder(index[root] + 1, inOrderLast, postOrderStart + left, postOrderLast - 1)


preOrder(0, n - 1, 0, n - 1)
print(*preOrderResult)