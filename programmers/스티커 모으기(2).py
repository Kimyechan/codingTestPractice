def solution(sticker):
    answer = 36

    n = len(sticker)
    if n == 1:
        return sticker[0]
    if n == 2:
        return max(sticker[0], sticker[1])

    dp1 = [0] * n
    dp2 = [0] * n
    dp3 = [0] * n

    dp1[0] = sticker[0]
    dp1[1] = sticker[0]
    for i in range(2, n - 1):
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + sticker[i])

    dp2[1] = sticker[1]
    dp2[2] = sticker[1]
    for i in range(3, n):
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + sticker[i])

    dp3[2] = sticker[2]
    for i in range(3, n):
        dp3[i] = max(dp3[i - 1], dp3[i - 2] + sticker[i])

    answer = max(dp1[n - 2], dp2[n - 1], dp3[n - 1])

    return answer