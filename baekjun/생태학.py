import sys
from collections import defaultdict

treeSet = set()
treeDict = defaultdict(int)
totalCount = 0
while True:
    tree = sys.stdin.readline().rstrip()
    if tree == "":
        break
    treeDict[tree] += 1
    treeSet.add(tree)
    totalCount += 1

treeList = list(treeSet)
treeList.sort()
for tree in treeList:
    percent = treeDict[tree] * 100 / totalCount
    print("%s %0.4f" % (tree, percent))