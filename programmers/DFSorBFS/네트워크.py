from collections import deque

network = 0
flag = 0


def bfs(start, n, computers, visited):
    global network
    global flag
    q = deque([start])
    if visited[start] == False:
        visited[start] = True
        flag = 1

    while q:
        v = q.popleft()
        visited[v] = True
        for i in range(n):
            if computers[v][i] == 1 and visited[i] == False:
                q.append(i)
                visited[i] = True
                flag = 1


def solution(n, computers):
    answer = 0
    visited = [False] * n
    global flag

    while False in visited:
        for i in range(n):
            bfs(i, n, computers, visited)
            if flag == 1:
                answer += 1
            flag = 0

    return answer


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
