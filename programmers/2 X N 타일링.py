def solution(n):
    T = [0 for i in range(n+1)]
    T[1] = 1
    T[2] = 2
    for i in range(3, n+1):
        T[i] = T[i-1] + T[i-2]
        T[i] %= 1000000007

    answer = T[n]
    return answer