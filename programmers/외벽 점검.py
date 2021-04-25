# check
# from itertools import permutations
#
#
# def solution(n, weak, dist):
#     L = len(weak)
#     cand = []
#     weak_point = weak + [w + n for w in weak]  # 선형으로
#
#     for i, start in enumerate(weak):
#         for friends in permutations(dist):  # 순열 이용
#             count = 1
#             position = start
#             # 친구 조합 배치
#             for friend in friends:
#                 position += friend
#                 # 끝 포인트까지 도달 못했을 때
#                 if position < weak_point[i + L - 1]:
#                     count += 1  # 친구 더 투입
#                     # 현재 위치보다 멀리 있는 취약지점 중 가장 가까운 위치로
#                     position = [w for w in weak_point[i + 1:i + L]
#                                 if w > position][0]
#                 else:  # 끝 포인트까지 도달
#                     cand.append(count)
#                     break
#
#     return min(cand) if cand else -1
#
#
# print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))

# from itertools import permutations
#
#
# def solution(n, weak, dist):
#     answer = 0
#     weakPoint = weak + [w + n for w in weak]
#     candidate = []
#     for idx, start in enumerate(weak):
#         for friends in permutations(dist):
#             count = 1
#             position = start
#             for friend in friends:
#                 position += friend
#                 if position < weakPoint[idx + len(weak) - 1]:
#                     count += 1
#                     for distW in weakPoint[idx + 1: idx + len(weak)]:
#                         if position < distW:
#                             position = distW
#                             break
#                 else:
#                     candidate.append(count)
#                     break
#
#     return min(candidate) if candidate else -1

from itertools import permutations


def solution(n, weak, dist):
    answer = []
    weakExtend = weak + [w + n for w in weak]

    for friends in permutations(dist):
        for weakIndex in range(len(weak)):
            position = weak[weakIndex]
            count = 1
            for friend in friends:
                if position + friend < weakExtend[weakIndex + len(weak) - 1]:
                    count += 1
                    for i in range(weakIndex, weakIndex + len(weak)):
                        if position + friend < weakExtend[i]:
                            position = weakExtend[i]
                            break
                else:
                    answer.append(count)

    if answer:
        return min(answer)
    else:
        return -1