def solution(n):
    F = [0] * (n + 1)
    F[1] = 1
    if n == 1:
        return F[1]
    else:
        for i in range(2, n + 1):
            F[i] = F[i - 1] + F[i - 2]
        return F[n] % 1234567