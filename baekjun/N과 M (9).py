import sys
from itertools import permutations


n, m = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))

permSet = set()
for perm in permutations(numbers, m):
    permSet.add(perm)

permList = list(permSet)
permList.sort()

for perm in permList:
    for p in perm:
        print(p, end=" ")
    print()