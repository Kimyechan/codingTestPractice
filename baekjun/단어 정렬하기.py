from collections import defaultdict

N = int(input())

strList = list()

for _ in range(N):
    strList.append(input())

strList = set(strList)
strList = list(strList)

newStrList = sorted(strList, key=lambda x: len(x))
d = defaultdict(list)

for ns in newStrList:
    if len(ns) in d.keys():
        d[len(ns)].append(ns)
        d[len(ns)].sort()
    else:
        d[len(ns)] = [ns]

result = list()

for s in d.values():
    result.extend(s)

for s in result:
    print(s)