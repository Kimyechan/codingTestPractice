# check
from copy import deepcopy


def solution(money):
    dp = [0] * (len(money) + 1)

    for idx, value in enumerate(money, start=1):
        dp[idx] = value

    if len(money) == 3:
        return max(dp)

    if len(money) == 4:
        return max(dp[1] + dp[3], dp[2] + dp[4])

    # 첫번째 집 선택 안 한 경우
    dp1 = deepcopy(dp)
    dp1[4] = dp1[4] + dp1[2]
    for i in range(5, len(money) + 1):
        dp1[i] += max(dp1[i - 2], dp1[i - 3])

    # 한 경우
    dp[3] += dp[1]
    dp[4] += dp[1]
    for i in range(5, len(money)):
        dp[i] += max(dp[i - 2], dp[i - 3])

    return max(dp1[len(money)], max(dp[len(money) - 1], dp[len(money) - 2]))


print(solution([1, 2, 3, 1, 5, 7, 3]))


# def solution(money):
#     answer = 0
#
#     dp1 = [] # 첫 집을 털었을 때
#     dp2 = [] # 첫 집을 안 털고 두 번째 집을 털었을 때
#     dp3 = [] # 첫 집과 두 번째 집을 안 털었을 때
#     for i in money:
#         dp1.append(0)
#         dp2.append(0)
#         dp3.append(0)
#     dp1[0] = money[0]
#     dp1[1] = dp1[0]
#     dp2[1] = money[1]
#
#     for i in range(2, len(money) - 1):
#         dp1[i] = max(dp1[i - 1], dp1[i - 2] + money[i])
#         dp2[i] = max(dp2[i - 1], dp2[i - 2] + money[i])
#         dp3[i] = max(dp3[i - 1], dp3[i - 2] + money[i])
#     e = len(money) - 1
#     dp1[e] = dp1[e - 1]
#     dp2[e] = max(dp2[e - 1], dp2[e - 2] + money[e])
#     dp3[e] = max(dp3[e - 1], dp3[e - 2] + money[e])
#     answer = max(dp1[e], dp2[e], dp3[e])
#
#     return answer