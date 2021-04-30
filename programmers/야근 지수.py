# check
import heapq


def solution(n, works):
    answer = 0
    hq = []
    for work in works:
        heapq.heappush(hq, (-work, work))

    while n > 0:
        work = heapq.heappop(hq)
        if work[1] <= 0:
            break

        newWork = work[1] - 1
        heapq.heappush(hq, (-newWork, newWork))
        n -= 1

    for work in list(hq):
        answer += work[1] ** 2

    return answer
