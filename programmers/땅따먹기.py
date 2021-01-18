def solution(land):
    dp = [[0 for _ in range(4)] for _ in range(len(land))]
    dp[0] = land[0]

    for i in range(1, len(land)):
        for j in range(4):
            prevMax = 0
            for z in range(4):
                if z != j and dp[i - 1][z] > prevMax:
                    prevMax = dp[i - 1][z]
            dp[i][j] = prevMax + land[i][j]

    return max(dp[len(land) - 1])