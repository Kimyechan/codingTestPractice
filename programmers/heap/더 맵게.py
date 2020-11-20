# https://programmers.co.kr/learn/courses/30/lessons/42626
# 나의 풀이
import heapq


def solution(scoville, K):
    answer = 0
    scoville.sort()

    while True:
        if scoville[0] >= K:
            break
        min1 = heapq.heappop(scoville)
        min2 = heapq.heappop(scoville)
        mixed_food = min1 + min2 * 2
        heapq.heappush(scoville, mixed_food)
        answer += 1

        if len(scoville) == 1 and scoville[0] < K:
            return -1

    return answer



# 다른 사람 풀이
# array 전체 처음에 heap으로 만들때 heapq.heapify(array)

# import heapq as hq
#
# def solution(scoville, K):
#
#     hq.heapify(scoville)
#     answer = 0
#     while True:
#         first = hq.heappop(scoville)
#         if first >= K:
#             break
#         if len(scoville) == 0:
#             return -1
#         second = hq.heappop(scoville)
#         hq.heappush(scoville, first + second*2)
#         answer += 1
#
#     return answer
