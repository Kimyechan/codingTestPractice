# https://programmers.co.kr/learn/courses/30/lessons/42627
# 못푼 문제 : 바로 실행 가능한 작업중 가장 작업시간이 짧은 작업 우선 처리(대기 시간 짧은거 말고)
import heapq


def solution(jobs):
    answer = 0
    jobs.sort()
    currentTime = jobs[0][0]
    prevCurrentTime = -1
    count = 0
    enableJobs = []

    while count < len(jobs):
        for job in jobs:
            if prevCurrentTime < job[0] <= currentTime:
                heapq.heappush(enableJobs, [job[1], job[0]])

        if enableJobs:
            prevCurrentTime = currentTime
            count += 1
            selectJob = heapq.heappop(enableJobs)
            currentTime += selectJob[0]
            answer += currentTime - selectJob[1]
        else:
            currentTime += 1

    return answer // len(jobs)


# import heapq
#
#
# def solution(jobs):
#     count, last, answer = 0, -1, 0
#     heap = []
#     jobs.sort()
#     # 시작시간 초기화
#     time = jobs[0][0]
#     while count < len(jobs):
#         for s, t in jobs:
#             if last < s <= time:
#                 # 작업 소요시간으로 min heap을 만들기 위해 (t, s) 푸시
#                 heapq.heappush(heap, (t, s))
#         # 바로 수행할 수 있는 작업이 있는 경우
#         if len(heap) > 0:
#             count += 1
#             last = time
#             term, start = heapq.heappop(heap)
#             time += term
#             answer += (time - start)
#         # 바로 수행할 수 있는 작업이 없는 경우
#         else:
#             time += 1
#     return answer//len(jobs)


print(solution([[0, 3], [1, 9], [2, 6]]))