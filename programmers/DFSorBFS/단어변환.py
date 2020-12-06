# hih -> hho 로 변환 될 수 있음체크 ( enumerate로 단어의 알파벳 위치까지 확인해야함)
import sys

sys.setrecursionlimit(100000)


def solution(begin, target, words):
    visited = [False] * len(words)

    if target not in words:
        return 0
    countList = []

    def dfs(tWord, count):
        if tWord == target:
            countList.append(count)
            return

        if False not in visited:
            return

        for x in enumerate(words):
            countI = 0
            countO = 0
            for y in enumerate(x[1]):
                if y in enumerate(tWord):
                    countI += 1
                else:
                    countO += 1
            if countI == len(x[1]) - 1 and countO == 1 and visited[x[0]] == False:
                visited[x[0]] = True
                dfs(x[1], count + 1)
                visited[x[0]] = False

    dfs(begin, 0)
    if countList:
        answer = min(countList)
    else:
        answer = 0
    return answer


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))