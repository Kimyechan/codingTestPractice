t = int(input())
for _ in range(t):
    n = int(input())

    if n == 1:
        print(1)
    elif n == 2:
        print(2)
    elif n == 3:
        print(4)
    else:
        way = [0] * (n + 1)
        way[1] = 1
        way[2] = 2
        way[3] = 4

        for i in range(4, n + 1):
            way[i] = way[i - 1] + way[i - 2] + way[i - 3]

        print(way[n])