# check check
# import heapq
#
#
# def solution(jobs):
#     answer = 0
#     start, now = -1, 0
#     enableJobs = []
#
#     jobCount = 0
#     while jobCount < len(jobs):
#         for job in jobs:
#             if start < job[0] <= now:
#                 heapq.heappush(enableJobs, [job[1], job[0]])
#
#         if len(enableJobs) != 0:
#             term, startJ = heapq.heappop(enableJobs)
#             start = now
#             now += term
#             answer += now - startJ
#             jobCount += 1
#         else:
#             now += 1
#
#     return answer // len(jobs)
#
#
# print(solution([[0, 3], [1, 9], [2, 6]]))
import heapq


def solution(jobs):
    jobs.sort(key=lambda x: (x[0], x[1]))

    currentTime = jobs[0][0]
    totalTime = 0
    checkUse = [False] * len(jobs)
    checkUse[0] = True
    count = 0

    q = [(jobs[0][1], jobs[0][0])]
    heapq.heapify(q)

    while count != len(jobs):
        if q:
            controller = heapq.heappop(q)
            currentTime += controller[0]
            totalTime += currentTime - controller[1]
            count += 1
        else:
            currentTime += 1

        for i in range(len(jobs)):
            if jobs[i][0] <= currentTime and not checkUse[i]:
                heapq.heappush(q, (jobs[i][1], jobs[i][0]))
                checkUse[i] = True

    return totalTime // len(jobs)


# print(solution([[0, 3], [1, 9], [2, 6]]))
print(solution([[0, 5], [2, 10], [30, 2]]))