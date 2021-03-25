from collections import deque

n, k = map(int, input().split())
q = deque([])

for i in range(1, n + 1):
    q.append(i)

result = []
while q:
    for _ in range(k - 1):
        q.append(q.popleft())

    result.append(q.popleft())

answer = "<"

for i in range(len(result) - 1):
    answer += str(result[i]) + ", "

answer += str(result[-1]) + ">"

print(answer)
