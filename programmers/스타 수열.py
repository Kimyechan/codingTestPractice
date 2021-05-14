# check
# from collections import Counter
#
#
# def solution(a):
#     answer = -1
#     elements = Counter(a)
#
#     for k in elements.keys():
#         if elements[k] <= answer:
#             continue
#         commonCnt = 0
#         idx = 0
#         while idx < len(a) - 1:
#             if (a[idx] != k and a[idx + 1] != k) or (a[idx] == a[idx + 1]):
#                 idx += 1
#                 continue
#             commonCnt += 1
#             idx += 2
#         answer = max(commonCnt, answer)
#
#     if answer == -1:
#         return 0
#     else:
#         return answer * 2

# from collections import Counter
#
#
# def solution(a):
#     answer = -1
#     numCount = Counter(a)
#
#     for k in numCount.keys():
#         if numCount[k] <= answer:
#             continue
#
#         starSeq = 0
#         idx = 0
#         while idx < len(a) - 1:
#             if (a[idx] != k and a[idx + 1] != k) or (a[idx] == a[idx + 1]):
#                 idx += 1
#                 continue
#             starSeq += 1
#             idx += 2
#
#         answer = max(answer, starSeq)
#
#     if answer == -1:
#         return 0
#     else:
#         return answer * 2

from collections import Counter


def solution(a):
    answer = -1
    numCount = Counter(a)

    for key in numCount.keys():
        if numCount[key] <= answer:
            continue

        idx = 0
        starLen = 0
        while idx < len(a) - 1:
            if (a[idx] != key and a[idx + 1] != key) or (a[idx] == a[idx + 1]):
                idx += 1
                continue
            idx += 2
            starLen += 1

        answer = max(answer, starLen)

    if answer == -1:
        return 0
    else:
        return answer * 2

    return answer