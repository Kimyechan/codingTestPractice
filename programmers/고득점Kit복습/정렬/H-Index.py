def solution(citations):
    answer = []
    citations.sort()
    maxH = citations[-1]

    for h in range(0, maxH + 1):
        stand = 0
        for i in range(len(citations)):
            if citations[i] >= h:
                stand = i
                break

        if len(citations) - stand >= h >= stand:
            answer.append(h)

    return answer[-1]


print(solution([3, 0, 6, 1, 5]))
print(solution([0, 1, 2]))
print(solution([2]))


# h는 최대 1000임 논문 수가 최대 1000 편 이하이기 때문에
# def solution(citations):
#     citations = sorted(citations)
#     l = len(citations)
#     for i in range(l):
#         if citations[i] >= l-i:
#             return l-i
#     return 0
#
#
# print(solution([3, 0, 6, 1, 5]))
