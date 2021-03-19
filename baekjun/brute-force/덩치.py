n = int(input())
people = [list(map(int, input().split())) for _ in range(n)]

result = []
for person in people:
    count = 0
    for compare in people:
        if person[0] < compare[0] and person[1] < compare[1]:
            count += 1

    result.append(count + 1)

for x in result:
    print(x, end=" ")