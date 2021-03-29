n = int(input())

numbers = list(map(int, input().split()))

dp1 = [1] * n

for i in range(n):
    for j in range(0, i):
        if numbers[j] < numbers[i]:
            dp1[i] = max(dp1[i], dp1[j] + 1)

numbers.reverse()

dp2 = [1] * n

for i in range(n):
    for j in range(0, i):
        if numbers[j] < numbers[i]:
            dp2[i] = max(dp2[i], dp2[j] + 1)

dp2.reverse()

result = [0] * n

for i in range(n):
    result[i] = dp1[i] + dp2[i]

print(max(result) - 1)