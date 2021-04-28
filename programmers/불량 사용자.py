# check
# from itertools import permutations
#
#
# def isMatch(user_set, banned_set):
#     for i in range(len(user_set)):
#         if len(user_set[i]) != len(banned_set[i]):
#             return False
#         for j in range(len(user_set[i])):
#             if banned_set[i][j] == '*':
#                 continue
#             if user_set[i][j] != banned_set[i][j]:
#                 return False
#     return True
#
#
# def solution(user_id, banned_id):
#     ans = []
#     for com_set in permutations(user_id, len(banned_id)):
#         if isMatch(com_set, banned_id):
#             com_set = set(com_set)  # 중복 제거
#             if com_set not in ans:
#                 ans.append(com_set)
#     return len(ans)
from copy import deepcopy

bannedList = []


def checkCandidate(userId, id):
    result = []
    for cand in userId:
        if len(cand) != len(id):
            continue
        correctFlag = True
        for idx, c in enumerate(list(cand)):
            if id[idx] == "*":
                continue
            if id[idx] != c:
                correctFlag = False
                break
        if correctFlag:
            result.append(cand)

    return result


def calcBannedList(user_id, banned_id, candList, index, candidate, visited):
    if index == len(banned_id):
        if set(candList) not in bannedList:
            bannedList.append(deepcopy(set(candList)))
        return

    for cand in candidate[index]:
        if not visited[cand]:
            candList.append(cand)
            visited[cand] = True
            calcBannedList(user_id, banned_id, candList, index + 1, candidate, visited)
            print(candList)
            visited[cand] = False
            candList.pop()


def solution(user_id, banned_id):
    candidate = []
    for id in banned_id:
        candidate.append(checkCandidate(user_id, id))

    visited = dict()
    for id in user_id:
        visited[id] = False

    calcBannedList(user_id, banned_id, [], 0, candidate, visited)
    print(bannedList)
    return len(bannedList)


# print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))
