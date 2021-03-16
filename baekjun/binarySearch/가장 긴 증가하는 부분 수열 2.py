N = int(input())
A = list(map(int, input().split()))

dp = [0]

for i in range(N):
    start = 0
    end = len(dp) - 1

    while start <= end:
        mid = (start + end) // 2

        if dp[mid] < A[i]:
            start = mid + 1
        else:
            end = mid - 1

    if start >= len(dp):
        dp.append(A[i])
    else:
        dp[start] = A[i]

print(len(dp) - 1)

