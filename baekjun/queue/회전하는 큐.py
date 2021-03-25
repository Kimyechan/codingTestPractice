from collections import deque

n, m = map(int, input().split())
order = list(map(int, input().split()))

q = []
for i in range(1, n + 1):
    q.append(i)

result = 0
for o in order:
    right = deque(q[:])
    left = deque(q[:])

    rightCount = 0
    while right[0] != o:
        right.appendleft(right.pop())
        rightCount += 1
    right.popleft()

    leftCount = 0
    while left[0] != o:
        left.append(left.popleft())
        leftCount += 1
    left.popleft()

    if rightCount < leftCount:
        q = list(right)
        result += rightCount
    else:
        q = list(left)
        result += leftCount

print(result)