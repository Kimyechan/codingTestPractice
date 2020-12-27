def solution(triangle):
    answer = 0
    if len(triangle) == 1:
        return triangle[0][0]

    h = len(triangle)
    dp = [[0 for _ in range(h)] for _ in range(h)]
    dp[0][0] = triangle[0][0]

    for i in range(1, h):
        for idx, value in enumerate(triangle[i]):
            if idx == 0:
                dp[i][idx] = dp[i - 1][idx] + value
            elif idx == len(triangle[i]) - 1:
                dp[i][idx] = dp[i - 1][idx - 1] + value
            else:
                if dp[i - 1][idx - 1] > dp[i - 1][idx]:
                    dp[i][idx] = dp[i - 1][idx - 1] + value
                else:
                    dp[i][idx] = dp[i - 1][idx] + value

    answer = max(dp[h-1])

    return answer

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))