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
