# check
# def solution(people, limit):
#     people.sort()
#
#     a = 0
#     b = len(people) - 1
#     boatCount = 0
#     while a <= b:
#         boatCount += 1
#         if people[a] + people[b] <= limit and a != b:
#             a += 1
#         b -= 1
#
#     return boatCount
#
#
# print(solution([70, 50, 80, 50], 100))
# print(solution([70, 80, 50], 100))
# print(solution([70, 50, 80, 50, 50, 60], 100))
# print(solution([50, 50, 50, 50], 100))
from collections import deque


def solution(people, limit):
    people.sort()
    q = deque(people)

    boatNeedCount = 0
    while q:
        maxWeight = q.pop()
        if len(q) != 0 and q[0] <= limit - maxWeight:
            q.popleft()

        boatNeedCount += 1

    return boatNeedCount


print(solution([70, 50, 80, 50], 100))

























