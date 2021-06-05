m = int(input())
stones = list(map(int, input().split()))
k = int(input())

totalStones = sum(stones)
result = 0
for stone in stones:
    if stone >= k:
        tempResultH = 1
        tempResultB = 1
        tempH = stone
        tempB = totalStones
        for i in range(k):
            tempResultH *= tempH
            tempResultB *= tempB
            tempH -= 1
            tempB -= 1
        result += tempResultH / tempResultB

print(result)