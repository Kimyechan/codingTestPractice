import sys

n = int(sys.stdin.readline())

distance = list(map(int, sys.stdin.readline().split()))
price = list(map(int, sys.stdin.readline().split()))

j = 0
totalCost = 0
for i in range(1, len(price)):
    if price[i] <= price[j]:
        for k in range(j, i):
            totalCost += distance[k] * price[j]
        j = i

if j < len(price) - 1:
    for k in range(j, len(price) - 1):
        totalCost += distance[k] * price[j]

print(totalCost)

# 5
# 1 1 1 1
# 1 2 3 2 1


# 5
# 1 1 1 1
# 5 4 3 2 1

# 5
# 1 1 1 1
# 5 4 3 4 5