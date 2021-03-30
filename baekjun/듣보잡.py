from collections import defaultdict
import sys

n, m = map(int, sys.stdin.readline().split())

nameDict = defaultdict(int)


result = []
for _ in range(n + m):
    name = sys.stdin.readline()[:-1]

    nameDict[name] = nameDict[name] + 1
    if nameDict[name] == 2:
        result.append(name)

result.sort()

print(len(result))
for name in result:
    print(name)