# check
import heapq


def solution(jobs):
    answer = 0
    start, now = -1, 0
    enableJobs = []

    jobCount = 0
    while jobCount < len(jobs):
        for job in jobs:
            if start < job[0] <= now:
                heapq.heappush(enableJobs, [job[1], job[0]])

        if len(enableJobs) != 0:
            term, startJ = heapq.heappop(enableJobs)
            start = now
            now += term
            answer += now - startJ
            jobCount += 1
        else:
            now += 1

    return answer // len(jobs)


print(solution([[0, 3], [1, 9], [2, 6]]))