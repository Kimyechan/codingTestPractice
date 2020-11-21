# https://programmers.co.kr/learn/courses/30/lessons/42628
# def solution(operations):
#     answer = []
#     array = []
#
#     for operation in operations:
#         if operation[0] == "I":
#             s = ""
#             for i in range(2, len(operation)):
#                 s += operation[i]
#             value = int(s)
#             array.append(value)
#             array.sort()
#         elif operation[0] == "D":
#             if array:
#                 if operation[2: len(operation)] == "1":
#                     array.pop(-1)
#                 elif operation[2: len(operation)] == "-1":
#                     array.pop(0)
#
#     if array:
#         answer = [array[-1], array[0]]
#     else:
#         answer = [0, 0]
#
#     return answer

import heapq

def solution(operations):
    answer = []
    heapMax = []
    heapMin = []
    countI = 0
    countD = 0

    for operation in operations:
        # 같으면 초기화 진행
        if countI == countD:
            heapMax = []
            heapMin = []

        if operation[0] == "I":
            s = ""
            for i in range(2, len(operation)):
                s += operation[i]
            value = int(s)
            heapq.heappush(heapMax, -1 * value)
            heapq.heappush(heapMin, value)
            countI += 1
        elif operation[0] == "D":
            if countI > countD:
                if operation[2: len(operation)] == "1":
                    heapq.heappop(heapMax)
                elif operation[2: len(operation)] == "-1":
                    heapq.heappop(heapMin)
                countD += 1
            else:
                heapMax = []
                heapMin = []

    if countI > countD:
        answer = [-1 * heapq.heappop(heapMax), heapq.heappop(heapMin)]
    else:
        answer = [0, 0]

    return answer


print(solution(["I 4", "I 3", "I 2", "I 1", "D 1", "D 1", "D -1", "D -1", "I 5", "I 6"]))