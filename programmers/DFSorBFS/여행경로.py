# 문제 잘못 읽음 -> 모든 항공사 지나는게 아니라 모든 항공권 사용임!!
import sys
import copy
sys.setrecursionlimit(100000)


def solution(tickets):
    answer = []
    route = {}
    visited = {}
    for ticket in tickets:
        if ticket[0] in route:
            route[ticket[0]].append(ticket[1])
            route[ticket[0]].sort()
            if not ticket[1] in route: # 종착지에 대한 해쉬 값을 만들어야 루프를 돌 때 error가 안 생김
                route[ticket[1]] = []
        else:
            route[ticket[0]] = [ticket[1]]
            if not ticket[1] in route:
                route[ticket[1]] = []

        if ticket[0] in visited:
            visited[ticket[0]].append(False)
        else:
            visited[ticket[0]] = [False]

    answer.append("ICN")
    result = []

    size = len(tickets)

    def dfs(v, count):
        if count == size:
            result.append(copy.deepcopy(answer))
            print(answer)
            return

        for index in range(len(route[v])):
            value = route[v]
            check = visited[v]
            if not check[index]:
                check[index] = True
                count += 1
                answer.append(value[index])
                dfs(value[index], count)
                check[index] = False
                count -= 1
                answer.pop(-1)

    dfs("ICN", 0)

    result.sort()
    answer = result[0]
    print(result)
    return answer


# print(solution([["ICN","A"],["ICN","A"],["A","ICN"]]))
# print(solution([["ICN","A"],["A","ICN"]]))
# print(solution([["ICN", "A"], ["ICN", "A"], ["ICN", "B"], ["B", "ICN"]]))
# print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]));
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))
# print(solution([["ICN", "A"], ["A", "C"], ["A", "D"], ["D", "B"], ["B", "A"]]))