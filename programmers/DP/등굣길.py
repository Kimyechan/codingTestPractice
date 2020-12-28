# 좌표 설정 제대로 하기!!! 좌표는 배열의 인덱스 반대
def solution(m, n, puddles):
    dp = [[0 for _ in range(m)] for _ in range(n)]

    col = m + 1
    row = n + 1

    if puddles:
        puddles.sort()
        if puddles[0][0] == 1:
            row = puddles[0][1]

        puddles.sort(key=lambda x: x[1])
        if puddles[0][1] == 1:
            col = puddles[0][0]

    for i in range(col - 1):
        dp[0][i] = 1

    for i in range(row - 1):
        dp[i][0] = 1

    for i in range(1, n):
        for j in range(1, m):
            if [j + 1, i + 1] in puddles:  # 좌표 설정 제대로 하기!!
                dp[i][j] = 0
            else:
                dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 1000000007

    answer = dp[n - 1][m - 1] % 1000000007

    return answer

print(solution(5, 4, [[1, 3], [1, 4], [4, 1], [3, 1], [3, 4]]))