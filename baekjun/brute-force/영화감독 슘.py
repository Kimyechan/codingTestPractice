n = int(input())

result = []
for num in range(666, 66666666 + 1):
    title = str(num)
    count = 0
    for x in title:
        if x == '6':
            count += 1
        else:
            count = 0

        if count == 3:
            result.append(title)

    if len(result) == n:
        break

print(result[n - 1])