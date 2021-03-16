N, M = map(int, input().split())
trees = list(map(int, input().split()))

start = 1
end = max(trees)

result = 0
while start <= end:
    mid = (start + end) // 2

    treeLen = 0
    for tree in trees:
        if tree - mid > 0:
            treeLen += tree - mid

    if treeLen >= M:
        start = mid + 1
        result = mid
    elif treeLen < M:
        end = mid - 1

print(result)