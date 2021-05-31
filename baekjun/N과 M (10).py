import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())

numbers = list(map(int, sys.stdin.readline().split()))
numbers.sort()

combiSet = set()
for combi in combinations(numbers, m):
    combiSet.add(combi)

combiList = list(combiSet)
combiList.sort()
for combi in combiList:
    for num in list(combi):
        print(num, end=" ")
    print()