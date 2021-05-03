# check
def solution(gems):
    n = len(gems)
    setLen = len(set(gems))
    answer = [0, n - 1]
    start = 0
    end = 0
    gemDict = dict()
    gemDict[gems[0]] = 1

    while start < n and end < n:
        if len(gemDict) == setLen: # len(set(gems)) -> setLen 매 번 계산해서 시간 초과나서 변경
            if answer[1] - answer[0] > end - start:
                answer = [start, end]
            if gemDict[gems[start]] == 1:
                del gemDict[gems[start]]
            else:
                gemDict[gems[start]] -= 1
            start += 1
        else:
            end += 1
            if end == n:
                break
            else:
                if gemDict.get(gems[end]) == None:
                    gemDict[gems[end]] = 1
                else:
                    gemDict[gems[end]] += 1

    answer = [answer[0] + 1, answer[1] + 1]
    return answer