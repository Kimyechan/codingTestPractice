# check
# from collections import deque
#
#
# s = input()
# t = input()
#
# candidate = deque([s])
# canChange = 0
#
# while True:
#     stringSelected = candidate.popleft()
#     if len(stringSelected) == len(t):
#         break
#
#     aAppend = stringSelected + "A"
#     if aAppend == t:
#         canChange = 1
#         break
#     else:
#         candidate.append(aAppend)
#
#     bAppendReverse = stringSelected + "B"
#     bAppendReverse = bAppendReverse[::-1]
#     if bAppendReverse == t:
#         canChange = 1
#         break
#     else:
#         candidate.append(bAppendReverse)
#
# print(canChange)


# import sys
# sys.setrecursionlimit(1000000)
#
# s = input()
# t = input()
# result = 0
#
#
# def checkCanChange(t, current):
#     global result
#     if len(current) == len(t):
#         if current == t:
#             result = 1
#         return
#
#     current.append("A")
#     checkCanChange(t, current)
#     current.pop()
#
#     current.append("B")
#     current.reverse()
#     checkCanChange(t, current)
#     current.reverse()
#     current.pop()
#
#
# checkCanChange(list(t), list(s))
# print(result)


import sys
sys.setrecursionlimit(1000000)

s = input()
t = input()
result = 0


def checkCanChange(s, t):
    global result
    if len(s) == len(t):
        if s == t:
            result = 1
        return

    if t[0] == "B":
        t.reverse()
        t.pop()
        checkCanChange(s, t)
        t.append("B")
        t.reverse()

    if t[-1] == "A":
        t.pop()
        checkCanChange(s, t)
        t.append("A")


checkCanChange(list(s), list(t))
print(result)