# check
from collections import defaultdict


def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()

    set1 = set()
    dict1 = defaultdict(int)
    for i in range(len(str1) - 1):
        isAlphabet = True
        for j in str1[i:i + 2]:
            if ord(j) < ord('a') or ord(j) > ord('z'):
                isAlphabet = False

        if isAlphabet:
            set1.add(str1[i:i + 2])
            dict1[str1[i:i + 2]] += 1

    set2 = set()
    dict2 = defaultdict(int)
    for i in range(len(str2) - 1):
        isAlphabet = True
        for j in str2[i:i + 2]:
            if ord(j) < ord('a') or ord(j) > ord('z'):
                isAlphabet = False

        if isAlphabet:
            set2.add(str2[i:i + 2])
            dict2[str2[i:i + 2]] += 1

    if not set1 and not set2:
        answer = 1 * 65536
    else:
        top = set1 & set2
        topLen = len(top)
        for i in list(top):
            topLen += min(dict1[i], dict2[i]) - 1
        bottom = set1 | set2
        bottomLen = len(bottom)
        for i in list(bottom):
            bottomLen += max(dict1[i], dict2[i]) - 1
        answer = 65536 * topLen // bottomLen

    return answer


print(solution("aa1+aa2", "AAAA12"))
print(solution("FRANCE", "french"))
print(solution("E=M*C^2", "e=m*c^2"))


# def solution(str1, str2):
#
#     list1 = [str1[n:n+2].lower() for n in range(len(str1)-1) if str1[n:n+2].isalpha()]
#     list2 = [str2[n:n+2].lower() for n in range(len(str2)-1) if str2[n:n+2].isalpha()]
#
#     tlist = set(list1) | set(list2)
#     res1 = [] #합집합
#     res2 = [] #교집합
#
#     if tlist:
#         for i in tlist:
#             res1.extend([i]*max(list1.count(i), list2.count(i)))
#             res2.extend([i]*min(list1.count(i), list2.count(i)))
#
#         answer = int(len(res2)/len(res1)*65536)
#         return answer
#
#     else:
#         return 65536

# import re
# import math
#
# def solution(str1, str2):
#     str1 = [str1[i:i+2].lower() for i in range(0, len(str1)-1) if not re.findall('[^a-zA-Z]+', str1[i:i+2])]
#     str2 = [str2[i:i+2].lower() for i in range(0, len(str2)-1) if not re.findall('[^a-zA-Z]+', str2[i:i+2])]
#
#     gyo = set(str1) & set(str2)
#     hap = set(str1) | set(str2)
#
#     if len(hap) == 0 :
#         return 65536
#
#     gyo_sum = sum([min(str1.count(gg), str2.count(gg)) for gg in gyo])
#     hap_sum = sum([max(str1.count(hh), str2.count(hh)) for hh in hap])
#
#     return math.floor((gyo_sum/hap_sum)*65536)