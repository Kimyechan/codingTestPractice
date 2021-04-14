# check
# m, n -> dp[n][m]
# def solution(m, n, puddles):
#     dp = [[0] * m for _ in range(n)]
#
#     for i in range(m):
#         dp[0][i] = 1
#
#     for i in range(n):
#         dp[i][0] = 1
#
#     for puddle in puddles:
#         if puddle[1] - 1 == 0:
#             for i in range(puddle[0] - 1, m):
#                 dp[puddle[1] - 1][i] = -1
#         elif puddle[0] - 1 == 0:
#             for i in range(puddle[1] - 1, n):
#                 dp[i][puddle[0] - 1] = -1
#         else:
#             dp[puddle[1] - 1][puddle[0] - 1] = -1
#
#     for i in range(1, m):
#         for j in range(1, n):
#             if dp[j][i] == -1:
#                 continue
#             left = dp[j - 1][i] if dp[j - 1][i] != -1 else 0
#             top = dp[j][i - 1] if dp[j][i - 1] != -1 else 0
#             dp[j][i] = (left + top) % 1000000007
#
#     return dp[n - 1][m - 1] % 1000000007
#
#
# print(solution(4, 3, [[2, 2], [1, 2], [2, 1]]))
# print(solution(5, 4, [[3, 4]]))


# def solution(m,n,puddles):
#     grid = [[0]*(m+1) for i in range(n+1)] #왼쪽, 위로 한줄씩 만들어서 IndexError 방지
#     if puddles != [[]]:                    #물이 잠긴 지역이 0일 수 있음
#         for a, b in puddles:
#             grid[b][a] = -1                #미리 -1로 체크
#     grid[1][1] = 1
#     for j in range(1,n+1):
#         for k in range(1,m+1):
#             if j == k == 1:                #(1,1)은 1로 만들어두고, 0이 되지 않도록
#                 continue
#             if grid[j][k] == -1:           #웅덩이는 0으로 만들어 다음 덧셈 때 영향끼치지 않게
#                 grid[j][k] = 0
#                 continue
#             grid[j][k] = (grid[j][k-1] + grid[j-1][k])%1000000007   #[a,b] = [a-1,b] + [a,b-1] 공식
#
#     return grid[n][m]


def solution(m, n, puddles):
    routes = [[0] * m for _ in range(n)]

    for i in range(n):
        routes[i][0] = 1

    for i in range(m):
        routes[0][i] = 1

    for puddle in puddles:
        if puddle[0] == 1: # m
            for i in range(puddle[1] - 1, n):
                routes[i][0] = -1
        elif puddle[1] == 1: # n
            for i in range(puddle[0] - 1, m):
                routes[0][i] = -1
        else:
            routes[puddle[1] - 1][puddle[0] - 1] = -1

    for i in range(1, n):
        for j in range(1, m):
            if routes[i][j] == 0:
                left = routes[i][j - 1] if routes[i][j - 1] != -1 else 0
                top = routes[i - 1][j] if routes[i - 1][j] != -1 else 0
                routes[i][j] = (left + top) % 1000000007

    return routes[n - 1][m - 1]


print(solution(4, 3, [[2, 2]]))






















