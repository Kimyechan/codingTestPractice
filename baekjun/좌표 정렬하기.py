N = int(input())

spot = list()

for _ in range(N):
    spot.append(list(map(int, input().split())))

sortedSpot = sorted(spot, key=lambda x: (x[1], x[0]))

for x, y in sortedSpot:
    print(str(x) + " " + str(y))