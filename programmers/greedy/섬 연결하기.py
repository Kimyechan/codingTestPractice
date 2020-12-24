def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2])

    parent = [i for i in range(n)]

    def union(a, b):
        a = find(a) # 부모 끼리 연결해야한다
        b = find(b)

        if a > b:
            parent[a] = b
        else:
            parent[b] = a

    def find(a):
        if parent[a] == a:
            return a
        else:
            return find(parent[a]) # 왜 리턴을 안했니????

    for cost in costs:
        if find(cost[0]) == find(cost[1]):
            continue
        else:
            union(cost[0], cost[1])
            answer += cost[2]

    return answer

print(solution(7, [[0, 5, 10], [0, 1, 29], [1, 2, 16], [1, 6, 15], [2, 3, 12], [3, 6, 18], [3, 4, 22], [4, 6, 25], [4, 5, 27]]))