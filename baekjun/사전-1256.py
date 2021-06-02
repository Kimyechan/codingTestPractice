# check
import sys

n, m, k = map(int, sys.stdin.readline().split())
arr = [[1] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        arr[i][j] = arr[i - 1][j] + arr[i][j - 1]  # a로 시작 or z로 시작

if arr[n][m] < k:
    print(-1)
else:
    result = ""
    while True:
        if n == 0 or m == 0:
            result += "z" * m
            result += "a" * n
            break

        flag = arr[n - 1][m]
        if k <= flag:
            result += "a"
            n -= 1
        else:
            result += "z"
            m -= 1
            k -= flag
    print(result)
