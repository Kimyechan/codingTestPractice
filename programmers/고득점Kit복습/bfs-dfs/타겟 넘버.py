def dfs(idx, numbers, target, result):
    if idx == len(numbers) and result == target:
        return 1

    if idx == len(numbers):
        return 0

    count1 = dfs(idx + 1, numbers, target, result + numbers[idx])
    count2 = dfs(idx + 1, numbers, target, result - numbers[idx])

    return count1 + count2


def solution(numbers, target):
    answer = dfs(0, numbers, target, 0)
    return answer

# count = 0
#
#
# def dfs(idx, numbers, target, result):
#     global count
#     if idx == len(numbers) and result == target:
#         count += 1
#         return
#
#     if idx == len(numbers):
#         return
#
#     dfs(idx + 1, numbers, target, result + numbers[idx])
#     dfs(idx + 1, numbers, target, result - numbers[idx])
#
#
# def solution(numbers, target):
#     dfs(0, numbers, target, 0)
#     return count


print(solution([1, 1, 1, 1, 1], 3))