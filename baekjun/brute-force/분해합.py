n = int(input())

result = []
for num in range(n):
    constructor = 0
    for x in str(num):
        constructor += int(x)
    constructor += num

    if constructor == n:
        result.append(num)

if len(result) == 0:
    print(0)
else:
    result.sort()
    print(result[0])