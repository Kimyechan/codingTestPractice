from collections import defaultdict


def solution(msg):
    answer = []
    index = defaultdict(int)
    for i in range(ord('A'), ord('Z') + 1):
        index[chr(i)] = i - 64

    currentIndex = 0
    nextIndex = 1
    currentMaxIndex = 26
    while True:
        while nextIndex <= len(msg) and index[msg[currentIndex:nextIndex]] != 0:
            nextIndex += 1

        if nextIndex > len(msg):
            nextIndex = len(msg)
            answer.append(index[msg[currentIndex:nextIndex]])
            break

        currentMaxIndex += 1
        index[msg[currentIndex:nextIndex]] = currentMaxIndex
        answer.append(index[msg[currentIndex:nextIndex - 1]])

        currentIndex = nextIndex - 1

    return answer


print(solution("KAKAO"))
print(solution("TOBEORNOTTOBEORTOBEORNOT"))
print(solution("ABABABABABABABAB"))
