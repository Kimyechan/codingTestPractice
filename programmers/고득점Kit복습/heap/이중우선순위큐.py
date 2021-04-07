from collections import defaultdict
import heapq


def solution(operations):
    answer = []
    maxHeap = []
    minHeap = []

    numCheck = defaultdict(int)
    numList = []
    for operation in operations:
        command = operation.split(" ")
        if command[0] == "I":
            heapq.heappush(minHeap, int(command[1]))
            heapq.heappush(maxHeap, -int(command[1]))
            numCheck[int(command[1])] += 1
            numList.append(int(command[1]))
        elif command[0] == "D" and command[1] == "1":
            if len(maxHeap) == 0:
                continue
            num = heapq.heappop(maxHeap)
            while numCheck[-num] == 0:
                if len(maxHeap) == 0:
                    break
                num = heapq.heappop(maxHeap)
            if numCheck[-num] != 0:
                numCheck[-num] -= 1
        elif command[0] == "D" and command[1] == "-1":
            if len(minHeap) == 0:
                continue
            num = heapq.heappop(minHeap)
            while numCheck[num] == 0:
                if len(minHeap) == 0:
                    break
                num = heapq.heappop(minHeap)
            if numCheck[num] != 0:
                numCheck[num] -= 1

    numRemain = []
    for num in numList:
        while numCheck[num] != 0:
            numCheck[num] -= 1
            numRemain.append(num)
    if len(numRemain) == 0:
        answer = [0, 0]
    else:
        numRemain.sort()
        answer = [numRemain[-1], numRemain[0]]

    return answer


# print(solution(["I 16","D 1"]))
print(solution(["I 7", "I 5", "I -5", "D -1"]))

# from heapq import heappush, heappop
#
# def solution(arguments):
#     max_heap = []
#     min_heap = []
#     for arg in arguments:
#         if arg == "D 1":
#             if max_heap != []:
#                 heappop(max_heap)
#                 if max_heap == [] or -max_heap[0] < min_heap[0]:
#                     min_heap = []
#                     max_heap = []
#         elif arg == "D -1":
#             if min_heap != []:
#                 heappop(min_heap)
#                 if min_heap == [] or -max_heap[0] < min_heap[0]:
#                     max_heap = []
#                     min_heap = []
#         else:
#             num = int(arg[2:])
#             heappush(max_heap, -num)
#             heappush(min_heap, num)
#     if min_heap == []:
#         return [0, 0]
#     return [-heappop(max_heap), heappop(min_heap)]
