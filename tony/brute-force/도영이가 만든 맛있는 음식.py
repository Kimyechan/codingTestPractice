# n = int(input())
# tastes = [list(map(int, input().split())) for _ in range(n)]
#
# resultTastes = []
# visited = [False] * n
#
#
# def calcTaste(n, tastes, currentCombi, start):
#     resultS = 1
#     resultB = 0
#     for current in currentCombi:
#         resultS *= current[0]
#         resultB += current[1]
#
#     if len(currentCombi) != 0:
#         resultTastes.append(abs(resultS - resultB))
#
#     for i in range(start, n):
#         if not visited[i]:
#             visited[i] = True
#             currentCombi.append(tastes[i])
#             calcTaste(n, tastes, currentCombi, start + 1)
#             currentCombi.pop()
#             visited[i] = False
#
#
# calcTaste(n, tastes, [], 0)
# print(min(resultTastes))
n = int(input())
tastes = [list(map(int, input().split())) for _ in range(n)]

resultTastes = []


def calcTaste(n, tastes, currentCombi, start):
    resultS = 1
    resultB = 0
    for current in currentCombi:
        resultS *= current[0]
        resultB += current[1]

    if len(currentCombi) != 0:
        resultTastes.append(abs(resultS - resultB))

    for i in range(start, n):
        currentCombi.append(tastes[i])
        calcTaste(n, tastes, currentCombi, i + 1)
        currentCombi.pop()


calcTaste(n, tastes, [], 0)
print(min(resultTastes))
