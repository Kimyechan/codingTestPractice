n = int(input())
a = list(map(int, input().split()))

s = list()
result = [0] * n
for i in range(n):
    if len(s) == 0:
        s.append([a[i], i])
    else:
        while True:
            if len(s) == 0:
                s.append([a[i], i])
                break

            if s[-1][0] < a[i]:
                nge = s.pop()
                result[nge[1]] = a[i]
            else:
                s.append([a[i], i])
                break

for remain in s:
    result[remain[1]] = -1

for nge in result:
    print(nge, end=" ")