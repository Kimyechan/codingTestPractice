from collections import deque


def solution(n, computers):
    answer = 0
    visited = [False] * n

    def bfs(start, computers, n):
        q = deque([start])
        visited[start] = True

        while q:
            v = q.popleft()

            for i in range(n):
                if computers[v][i] == 1 and not visited[i]:
                    visited[i] = True
                    q.append(i)

    for i in range(n):
        if not visited[i]:
            bfs(i, computers, n)
            answer += 1

    return answer
