def solution(nums):
    numKind = set(nums)

    half = len(nums) // 2
    totalKind = len(numKind)

    if half < totalKind:
        answer = half
    else:
        answer = totalKind

    return answer


print(solution([3,1,2,3]))