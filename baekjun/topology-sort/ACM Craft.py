import heapq
import sys

t = int(input())

for _ in range(t):
    n, k = map(int, sys.stdin.readline().split())
    time = list(map(int, sys.stdin.readline().split()))

    order = [[] for _ in range(n + 1)]
    inDegree = [0] * (n + 1)

    for _ in range(k):
        a, b = map(int, sys.stdin.readline().split())
        order[a].append(b)
        inDegree[b] += 1

    q = []
    for i in range(1, n + 1):
        if inDegree[i] == 0:
            heapq.heappush(q, (time[i - 1], i))

    finalBuilding = int(input())

    totalTime = 0
    while q:
        building = heapq.heappop(q)
        maxTime = building[0]

        if building[1] == finalBuilding:
            totalTime = building[0]

        for nextB in order[building[1]]:
            inDegree[nextB] -= 1
            if inDegree[nextB] == 0:
                heapq.heappush(q, (time[nextB - 1] + building[0], nextB))

    print(totalTime)
