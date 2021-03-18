import sys
from collections import deque

n = int(input())
exp = input()
res = sys.maxsize * -1
check = [0] * n


def cal2(n1, op, n2):
    if op == '+':
        return n1 + n2
    elif op == '-':
        return n1 - n2
    else:
        return n1 * n2


def calc():
    q = deque([])
    i = 0
    while True:
        if i == n:
            break

        if i % 2 != 0 and check[i]:
            q.append(cal2(int(q.pop()), exp[i], int(exp[i + 1])))
            i += 1
        else:
            q.append(exp[i])
        i += 1
    while q:
        if len(q) == 1:
            break
        q.appendleft(cal2(int(q.popleft()), q.popleft(), int(q.popleft())))
    return q[0]


def solve(pos):
    global res
    if pos >= n:
        return calc()
    check[pos] = 1
    res = max(res, solve(pos + 4))
    check[pos] = 0
    res = max(res, solve(pos + 2))
    return res


print(solve(1))


















