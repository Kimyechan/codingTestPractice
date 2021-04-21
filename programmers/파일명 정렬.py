from functools import cmp_to_key

originalOrder = dict()


def parse(s):
    head = ''
    number = ''
    tail = ''

    s = s.lower()
    hIndex = 0
    for i in range(len(s)):
        if ord('z') >= ord(s[i]) >= ord('a') or s[i] in (" ", "-", "."):
            head += s[i]
            hIndex += 1
        else:
            break

    nIndex = hIndex
    for i in range(nIndex, len(s)):
        try:
            tempNum = int(s[i])
            number += str(tempNum)
            nIndex += 1
            if nIndex - hIndex > 5:
                break
        except:
            break

    tail += s[nIndex:]

    return [head, number, tail]


def compare(s1, s2):
    sParse1 = parse(s1)
    sParse2 = parse(s2)

    headSort = sorted([sParse1[0], sParse2[0]])
    if sParse1[0] == sParse2[0]:
        if int(sParse1[1]) - int(sParse2[1]) > 0:
            return 1
        elif int(sParse1[1]) - int(sParse2[1]) < 0:
            return -1
        else:
            if originalOrder[s1] - originalOrder[s2] > 0:
                return 1
            else:
                return -1
    elif sParse1[0] == headSort[0]:
        return -1
    elif sParse2[0] == headSort[0]:
        return 1


def solution(files):
    for idx, file in enumerate(files):
        originalOrder[file] = idx

    files.sort(key=cmp_to_key(compare))
    return files


print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))


# def solution(files):
#     answer = []
#     for f in files:
#         head, number, tail = '', '', ''
#
#         number_check = False
#         for i in range(len(f)): # 문자열 자르기
#             if f[i].isdigit():  # 처음 나오는 숫자부터는 NUMBER로
#                 number += f[i]
#                 number_check = True
#             elif not number_check:  # NUMBER가 나오기 전까지는 HEAD
#                 head += f[i]
#             else:               # NUMBER가 이미 나왔고, 숫자가 아닌 문자가 나오면 TAIL
#                 tail = f[i:]
#                 break
#         answer.append((head, number, tail))  # HEAD, NUMBER, TAIL 하나의 튜플로 저장
#
#     answer.sort(key=lambda x: (x[0].upper(), int(x[1])))  # HEAD 우선, NUMBER 차선으로 정렬
#
#     return [''.join(t) for t in answer]   # 원래 형태로 문자열 만들어서 반환