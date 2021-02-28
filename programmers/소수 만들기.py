from itertools import combinations

def solution(nums):
    count = 0

    for num in combinations(nums, 3):
        value = 0
        for x in num:
            value += x
        flag = 0
        for i in range(2, int(value ** 0.5) + 1):
            if value % i == 0:
                flag = 1
        if flag == 0:
            count += 1

    return count


print(solution([1, 2, 7, 6, 4]))
