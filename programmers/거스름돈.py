def solution(n, money):
    dp = [0] * (n + 1)
    for m in money:
        if m > n:
            continue
        for i in range(m, n + 1):
            if i == m:
                dp[i] += 1
            else:
                dp[i] += dp[i - m]

    return dp[n]