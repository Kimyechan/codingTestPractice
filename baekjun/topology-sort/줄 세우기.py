# from collections import deque
#
# n, m = map(int, input().split())
# orders = [list(map(int, input().split())) for _ in range(m)]
#
# q = deque([])
#
# degree = [0] * (n + 1)
# line = [[] for i in range(n + 1)]
#
# for order in orders:
#     line[order[0]].append(order[1])
#     degree[order[1]] += 1
#
# for student in range(1, n + 1):
#     if degree[student] == 0:
#         q.append(student)
#
# while q:
#     currentStudent = q.popleft()
#     print(currentStudent, end=" ")
#
#     for nextStudent in line[currentStudent]:
#         degree[nextStudent] = degree[nextStudent] - 1
#         if degree[nextStudent] == 0:
#             q.append(nextStudent)
from collections import deque
import sys

n, m = map(int, input().split())

q = deque([])

degree = [0] * (n + 1)
line = [[] for i in range(n + 1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    line[a].append(b)
    degree[b] += 1

for student in range(1, n + 1):
    if degree[student] == 0:
        q.append(student)

while q:
    currentStudent = q.popleft()
    print(currentStudent, end=" ")

    for nextStudent in line[currentStudent]:
        degree[nextStudent] = degree[nextStudent] - 1
        if degree[nextStudent] == 0:
            q.append(nextStudent)