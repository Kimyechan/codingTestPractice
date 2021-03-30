import sys

n = int(input())

schedule = []
for _ in range(n):
    schedule.append(list(map(int, sys.stdin.readline().split())))

schedule.sort(key=lambda x: (x[1], x[0]))

result = 0
endTime = 0
for i in range(n):
    if schedule[i][0] >= endTime:
        result += 1
        endTime = schedule[i][1]

print(result)