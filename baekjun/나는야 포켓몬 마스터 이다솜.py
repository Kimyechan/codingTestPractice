import sys

n, m = map(int, input().split())

nameMap = dict()
numMap = dict()
for i in range(1, n + 1):
    poketmon = sys.stdin.readline()[:-1]

    nameMap[poketmon] = i
    numMap[i] = poketmon

for i in range(m):
    command = sys.stdin.readline()[:-1]
    try:
        value = int(command)
        print(numMap[value])
    except:
        print(nameMap[command])
