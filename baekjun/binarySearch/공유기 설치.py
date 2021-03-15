N, C = map(int, input().split())

spot = list()
for _ in range(N):
    spot.append(int(input()))
spot.sort()

start = 1
end = spot[-1] - spot[0]
result = 0

while start <= end:
    mid = (start + end) // 2
    stand = spot[0]
    count = 1

    for i in range(1, len(spot)):
        if spot[i] >= stand + mid:
            stand = spot[i]
            count += 1

    if count >= C:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)


n, c = list(map(int, input().split(' ')))

array = list()
for _ in range(n):
    array.append(int(input()))
array = sorted(array)

start = 1
end = array[-1] - array[0]
result = 0

while start <= end:
    mid = (start + end) // 2
    value = array[0]
    count = 1

    for i in range(1, len(array)):
        if array[i] >= value + mid:
            value = array[i]
            count += 1
    if count >= c:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)