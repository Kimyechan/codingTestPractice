from itertools import combinations
import sys

n = int(input())
powers = [list(map(int, input().split())) for _ in range(n)]

players = set([i for i in range(n)])

result = sys.maxsize

for i in range(1, n // 2 + 1):
    for linkTeam in combinations(players, i):
        startPower = 0
        linkPower = 0

        startTeam = players - set(linkTeam)

        for p in linkTeam:
            for c in linkTeam:
                linkPower += powers[p][c]

        for p in startTeam:
            for c in startTeam:
                startPower += powers[p][c]

        result = min(result, abs(linkPower - startPower))


print(result)
