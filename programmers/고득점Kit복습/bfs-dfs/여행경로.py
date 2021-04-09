# newRoute = []
#
#
# def dfs(tickets, visited, start, route):
#     global newRoute
#     if len(route) == len(tickets) + 1:
#         if not newRoute:
#             newRoute = route[:]
#             return
#         for i in range(len(route)):
#             if newRoute[i] == route[i]:
#                 continue
#             if route[i] == sorted([newRoute[i], route[i]])[0]:
#                 newRoute = route[:]
#             break
#         return
#
#     for idx, ticket in enumerate(tickets):
#         if tickets[idx][0] == start and not visited[idx]:
#             visited[idx] = True
#             route.append(tickets[idx][1])
#             dfs(tickets, visited, tickets[idx][1], route)
#             route.pop()
#             visited[idx] = False
#
#
# def solution(tickets):
#     visited = [False] * len(tickets)
#     dfs(tickets, visited, "ICN", ["ICN"])
#     print(sorted(["ICN", "SFO"])[0])
#     return newRoute


# def solution(tickets):
#     routes = {}
#     for t in tickets:
#         routes[t[0]] = routes.get(t[0], []) + [t[1]]
#     for r in routes:
#         routes[r].sort(reverse=True)
#     stack = ['ICN']
#     path = []
#     while stack:
#         top = stack[-1]
#         if top in routes and routes[top]:
#             stack.append(routes[top].pop())
#         else:
#             path.append(stack.pop())
#     return path[::-1]
# # print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
# print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))

# from collections import deque
# from collections import defaultdict
#
#
# def solution(tickets):
#     route = defaultdict(list)
#     for ticket in tickets:
#         route[ticket[0]].append(ticket[1])
#
#     for ticket in tickets:
#         route[ticket[0]].sort()
#
#     answer = ["ICN"]
#     q = deque([route["ICN"].pop(0)])
#
#     while q:
#         location = q.popleft()
#
#         answer.append(location)
#         if location not in route.keys() or route[location] == []:
#             break
#         else:
#             q.append(route[location].pop(0))
#
#     return answer

# print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))
# print(solution([["ICN", "A"], ["ICN", "B"], ["B", "ICN"]])) #["ICN", "B", "ICN", "A"]


newRoute = []


def dfs(tickets, visited, start, route):
    if len(newRoute) == 1:
        return

    if len(route) == len(tickets) + 1:
        return newRoute.append(route[:])

    for idx, ticket in enumerate(tickets):
        if tickets[idx][0] == start and not visited[idx]:
            visited[idx] = True
            route.append(tickets[idx][1])
            dfs(tickets, visited, tickets[idx][1], route)
            route.pop()
            visited[idx] = False


def solution(tickets):
    visited = [False] * len(tickets)
    tickets.sort(key=lambda x: (x[0], x[1]))
    dfs(tickets, visited, "ICN", ["ICN"])
    return newRoute[0]


print(solution([["ICN", "A"], ["ICN", "B"], ["B", "ICN"]])) #["ICN", "B", "ICN", "A"]













