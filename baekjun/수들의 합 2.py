import sys

n, m = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

result = 0
aSum = a[0]
start = 0
end = 0
while start < n and end < n:
    if aSum < m:
        end += 1
        if end == n:
            break
        aSum += a[end]
    else:
        if aSum == m:
            result += 1
        aSum -= a[start]
        start += 1

print(result)