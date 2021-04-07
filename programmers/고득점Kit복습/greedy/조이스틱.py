# check
# def solution(name):
#     alphabetOrder = [chr(ord('A') + i) for i in range(26)]
#
#     name = list(name)
#     defaultName = list("A" * len(name))
#
#     i = 0
#     numMoveTotal = 0
#     while defaultName != name:
#         numMoveUp = alphabetOrder.index(name[i])
#         numMoveDown = 26 - alphabetOrder.index(name[i])
#
#         if numMoveUp > numMoveDown:
#             numMoveTotal += numMoveDown
#         else:
#             numMoveTotal += numMoveUp
#         defaultName[i] = name[i]
#
#         if defaultName == name:
#             break
#
#         # 왼쪽 오른쪽중 더 가까운 쪽 먼저 이동
#         nextMoveR = 0
#         start = i
#         for _ in range(len(name)):
#             start += 1
#             nextMoveR += 1
#             if start == len(name):
#                 start = 0
#             if defaultName[start] != name[start]:
#                 break
#
#         nextMoveL = 0
#         start = i
#         for _ in range(len(name)):
#             start -= 1
#             nextMoveL += 1
#             if start == len(name):
#                 start = 0
#             if defaultName[start] != name[start]:
#                 break
#
#         if nextMoveR <= nextMoveL:
#             numMoveTotal += nextMoveR
#             i += nextMoveR
#         else:
#             numMoveTotal += nextMoveL
#             i -= nextMoveL
#
#     return numMoveTotal


# print(solution("JAZ"))
# print(solution("JEROEN"))
# print(solution("JAN"))
# print(solution("AAABAAA"))
# print(solution("AAABBAAAB"))
# print(solution("BBBAAAB"))#9
# print(solution("ABABAAAAABA")) #11


def solution(name):
    make_name = [min(ord(i) - ord("A"), ord("Z") - ord(i) + 1) for i in name]
    idx, answer = 0, 0
    while True:
        answer += make_name[idx]
        make_name[idx] = 0
        if sum(make_name) == 0:
            break
        left, right = 1, 1
        while make_name[idx - left] == 0:
            left += 1
        while make_name[(idx + right) % len(name)] == 0:
            right += 1

        answer += left if left < right else right
        idx += -left if left < right else right

    return answer












