from collections import deque


def solution(s):
    answer = 0
    openClosed = deque(list(s))

    for _ in range(len(s)):
        tempS = list(openClosed)
        stack = []

        for i in range(len(tempS)):
            if len(stack) == 0:
                stack.append(tempS[i])
            else:
                if (stack[-1] == "(" and tempS[i] == ")") or (stack[-1] == "[" and tempS[i] == "]") or (stack[-1] == "{" and tempS[i] == "}"):
                    stack.pop()
                else:
                    stack.append(tempS[i])

        if len(stack) == 0:
            answer += 1

        openClosed.append(openClosed.popleft())

    return answer


print(solution("[](){}"))
print(solution("}]()[{"))
print(solution("[)(]"))
print(solution("}}}"))
