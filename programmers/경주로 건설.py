# check
# import sys
#
# sys.setrecursionlimit(10 ** 9)
#
#
# def solution(board):
#     answer = 0
#     arrows = [[0, 1], [0, -1], [1, 0], [-1, 0]]
#
#     visit = [list([False] * len(board)) for _ in range(len(board))]
#     result = []
#
#     def dfs(node, direction, visited, cost):
#         if node == (len(board) - 1, len(board) - 1):
#             result.append(cost)
#             return
#
#         for arrow in arrows:
#             if node[0] + arrow[0] < 0 or node[0] + arrow[0] >= len(board) or node[1] + arrow[1] < 0 or node[1] + arrow[
#                 1] >= len(board):
#                 continue
#             if board[node[0] + arrow[0]][node[1] + arrow[1]] != 0 or visited[node[0] + arrow[0]][node[1] + arrow[1]]:
#                 continue
#             if arrow in [[0, 1], [0, -1]]:
#                 if direction == 1:
#                     cost += 100
#                     visited[node[0] + arrow[0]][node[1] + arrow[1]] = True
#                     dfs((node[0] + arrow[0], node[1] + arrow[1]), 1, visited, cost)
#                     cost -= 100
#                     visited[node[0] + arrow[0]][node[1] + arrow[1]] = False
#                 else:
#                     cost += 600
#                     visited[node[0] + arrow[0]][node[1] + arrow[1]] = True
#                     dfs((node[0] + arrow[0], node[1] + arrow[1]), 1, visited, cost)
#                     cost -= 600
#                     visited[node[0] + arrow[0]][node[1] + arrow[1]] = False
#             else:
#                 if direction == 1:
#                     cost += 600
#                     visited[node[0] + arrow[0]][node[1] + arrow[1]] = True
#                     dfs((node[0] + arrow[0], node[1] + arrow[1]), 0, visited, cost)
#                     cost -= 600
#                     visited[node[0] + arrow[0]][node[1] + arrow[1]] = False
#                 else:
#                     cost += 100
#                     visited[node[0] + arrow[0]][node[1] + arrow[1]] = True
#                     dfs((node[0] + arrow[0], node[1] + arrow[1]), 0, visited, cost)
#                     cost -= 100
#                     visited[node[0] + arrow[0]][node[1] + arrow[1]] = False
#
#     dfs([0, 0], 0, visit, 0)
#     dfs([0, 0], 1, visit, 0)
#
#     result.sort()
#
#     return result[0]

# print(solution([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))
# print(solution([[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0],
#                 [0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 1, 0, 0],
#                 [1, 0, 0, 0, 0, 0, 0, 0]]))
# print(solution([[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]]))
# print(solution([[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 1, 0, 0, 0], [1, 0, 0, 1, 0, 1], [0, 1, 0, 0, 0, 1],
#                 [0, 0, 0, 0, 0, 0]]))


from collections import deque


def solution(board):
    answer = 0
    costTable = [list([float('inf')] * len(board)) for _ in range(len(board))]

    direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    q = deque([])
    costTable[0][0] = 0
    if board[1][0] == 0:
        q.append((1, 0, 2, 100))
        costTable[1][0] = 100
    if board[0][1] == 0:
        q.append((0, 1, 0, 100))
        costTable[0][1] = 100

    while q:
        x, y, arrow, cost = q.popleft()

        for idx, (nx, ny) in enumerate(direction):
            if x + nx < 0 or x + nx >= len(board) or y + ny < 0 or y + ny >= len(board):
                continue
            if board[x + nx][y + ny] != 0:
                continue

            newCost = cost
            if arrow in [0, 1]:
                if idx in [0, 1]:
                    newCost += 100
                else:
                    newCost += 600
            else:
                if idx in [2, 3]:
                    newCost += 100
                else:
                    newCost += 600

            if costTable[x + nx][y + ny] >= newCost:
                costTable[x + nx][y + ny] = newCost
                q.append((x + nx, y + ny, idx, newCost))

    print(costTable)
    return costTable[len(board) - 1][len(board) - 1]


# print(solution([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))
print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))






