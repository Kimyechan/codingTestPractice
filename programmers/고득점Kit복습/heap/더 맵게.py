import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    repeat = 0
    while scoville:
        score = heapq.heappop(scoville)

        if score >= K:
            heapq.heappush(scoville, score)
            break
        else:
            if len(scoville) == 0:
                break
            repeat += 1
            scoreNext = heapq.heappop(scoville)
            heapq.heappush(scoville, score + scoreNext * 2)

    if len(scoville) == 0:
        answer = -1
    else:
        answer = repeat

    return answer

print(solution([1, 2, 3, 9, 10, 12], 7))