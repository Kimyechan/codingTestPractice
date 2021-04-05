from collections import defaultdict


def solution(participant, completion):
    participantDict = defaultdict(int)

    for p in participant:
        participantDict[p] += 1

    for c in completion:
        participantDict[c] -= 1

    answer = ''
    for key, value in participantDict.items():
        if value == 1:
            answer = key
            break

    return answer


# collections.Counter 사용
# import collections
#
#
# def solution(participant, completion):
#     A = collections.Counter(participant)
#     B = collections.Counter(completion)
#     answer = collections.Counter(participant) - collections.Counter(completion)
#     return list(answer.keys())[0]
#
#
# print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))