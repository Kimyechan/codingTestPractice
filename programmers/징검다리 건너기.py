# check
def solution(stones, k):
    start = 1
    end = max(stones)

    while start < end:
        mid = (start + end) // 2

        stonesTemp = stones[:]
        count = 0
        flag = False
        for stone in stonesTemp:
            if stone - mid <= 0:
                count += 1
            else:
                count = 0
            if count == k:
                flag = True
                break

        if flag:
            end = mid
        else:
            start = mid + 1

    return end