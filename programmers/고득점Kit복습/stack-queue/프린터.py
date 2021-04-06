from collections import deque


def solution(priorities, location):
    answer = 0
    prioritiesWithIdx = deque([(value, idx) for idx, value in enumerate(priorities)])

    rank = 1
    while prioritiesWithIdx != 0:
        front = prioritiesWithIdx[0]

        flag = 0
        for i in range(1, len(prioritiesWithIdx)):
            if prioritiesWithIdx[i][0] > front[0]:
                flag = 1
                break

        if flag == 1:
            temp = prioritiesWithIdx.popleft()
            prioritiesWithIdx.append(temp)
        else:
            value = prioritiesWithIdx.popleft()
            if value[1] == location:
                answer = rank
                break
            rank += 1

    return answer


# any, all 함수
# def solution(priorities, location):
#     queue =  [(i,p) for i,p in enumerate(priorities)]
#     answer = 0
#     while True:
#         cur = queue.pop(0)
#         if any(cur[1] < q[1] for q in queue):
#             queue.append(cur)
#         else:
#             answer += 1
#             if cur[0] == location:
#                 return answer
#
#
# print(solution([2, 1, 3, 2], 2))
