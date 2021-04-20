# check
# from itertools import permutations
#
#
# def solution(expression):
#     operations = ["*", "-", "+"]
#     orders = []
#     for order in permutations(operations, 3):
#         orders.append(list(order))
#
#     calcList = []
#
#     q = []
#
#     tempNum = ""
#     for c in expression:
#         if c in ['*', '-', '+']:
#             q.append(tempNum)
#             tempNum = ""
#             q.append(c)
#         else:
#             tempNum += c
#     q.append(tempNum)
#
#     for order in orders:
#         tempQ = q[:]
#
#         for oper in order:
#             try:
#                 index = tempQ.index(oper)
#             except ValueError:
#                 continue
#
#             while True:
#                 a = tempQ.pop(index - 1)
#                 b = tempQ.pop(index - 1)
#                 c = tempQ.pop(index - 1)
#                 tempQ.insert(index - 1, str(eval(a + b + c)))
#                 try:
#                     index = tempQ.index(oper)
#                 except ValueError:
#                     break
#
#         calcList.append(abs(int(tempQ.pop())))
#     return max(calcList)
#
#
# print(solution("100-200*300-500+20"))

import re
from itertools import permutations


def solution(expression):
    # 1
    op = [x for x in ['*', '+', '-'] if x in expression]
    op = [list(y) for y in permutations(op)]
    ex = re.split(r'(\D)', expression)

    # 2
    a = []
    for x in op:
        _ex = ex[:]
        for y in x:
            while y in _ex:
                tmp = _ex.index(y)
                _ex[tmp - 1] = str(eval(_ex[tmp - 1] + _ex[tmp] + _ex[tmp + 1]))
                _ex = _ex[:tmp] + _ex[tmp + 2:]
        a.append(_ex[-1])

    # 3
    return max(abs(int(x)) for x in a)


print(solution("100-200*300-500+20"))
