import sys
import copy

sys.setrecursionlimit(100000)

operatorList = []


# def dfs(operators, count):
#     if len(operators) == count:
#         operatorList.append(copy.deepcopy(operators))
#         return
#
#     for x in [1, -1]:
#         operators.append(x)
#         dfs(operators, count)
#         operators.pop()
#
#
# def solution(numbers, target):
#     answer = 0
#     count = len(numbers)
#
#     operators = []
#
#     dfs(operators, count)
#     for operation in operatorList:
#         result = 0
#         for i in range(len(operation)):
#             result += operation[i] * numbers[i]
#         if result == target:
#             answer += 1
#
#     return answer

answer = 0

def dfs(numbers, target, sum, index):
    global answer
    if index == len(numbers):
        if sum == target:
            answer += 1
        return

    dfs(numbers, target, sum + numbers[index], index + 1)
    dfs(numbers, target, sum - numbers[index], index + 1)


def solution(numbers, target):
    dfs(numbers, target, 0, 0)

    return answer


print(solution([1, 1, 1, 1, 1], 3))