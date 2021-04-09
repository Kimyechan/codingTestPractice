# result = []
#
#
# def dfs(begin, target, words, level, visited):
#     if begin == target:
#         result.append(level)
#         return
#
#     for i in range(len(words)):
#         diffCount = 0
#         for j in range(len(begin)):
#             if begin[j] != words[i][j]:
#                 diffCount += 1
#         if diffCount == 1 and not visited[i]:
#             visited[i] = True
#             dfs(words[i], target, words, level + 1, visited)
#             visited[i] = False
#
#
# def solution(begin, target, words):
#     visited = [False] * len(words)
#     dfs(begin, target, words, 0, visited)
#
#     if not result:
#         answer = 0
#     else:
#         answer = min(result)
#
#     return answer
#
#
# print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))

from collections import deque


def solution(begin, target, words):
    answer = 0

    level = dict()
    level[begin] = 0

    q = deque([begin])

    while q:
        nextWord = q.popleft()

        for word in words:
            diffCount = 0
            for i in range(len(word)):
                if nextWord[i] != word[i]:
                    diffCount += 1
            if word not in level and diffCount == 1:
                level[word] = level[nextWord] + 1
                q.append(word)
                if word == target:
                    return level[word]

    return 0


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))













