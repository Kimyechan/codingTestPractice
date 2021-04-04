from collections import defaultdict
from collections import deque
from copy import deepcopy

cardOrders = []
orderVisited = []


# 카드 순서 정하기
def setCardOrder(cardList, order, visited):
    if len(cardList) == len(order):
        cardOrders.append(order[:])
        # print(order)

    for i in range(len(cardList)):
        if not visited[i]:
            visited[i] = True
            order.append(cardList[i])
            setCardOrder(cardList, order, visited)
            visited[i] = False
            order.remove(cardList[i])


# 같은 카드 순서 정하기
def setSameCardOrder(cardOrder, cardSpots, result, orderCount):
    if orderCount == len(cardOrder):
        orderVisited.append(result[:])
        # print(result)
        return

    spot = cardSpots[cardOrder[orderCount]]

    result.append(spot[0])
    result.append(spot[1])
    setSameCardOrder(cardOrder, cardSpots, result, orderCount + 1)
    result.pop()
    result.pop()

    result.append(spot[1])
    result.append(spot[0])
    setSameCardOrder(cardOrder, cardSpots, result, orderCount + 1)
    result.pop()
    result.pop()


def getCardSpotAsDict(board):
    cardSpots = defaultdict(list)
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                cardSpots[board[i][j]].append([i, j])
    return cardSpots


def bfs(cardVisitOrder, board, r, c):
    newBoard = deepcopy(board)
    visited = [[False] * 4 for _ in range(4)]
    visited[r][c] = True
    start = [r, c, 0]
    q = deque([start])

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    orderNum = 0
    distance = 0

    while q:
        spot = q.popleft()

        if spot[0] == cardVisitOrder[orderNum][0] and spot[1] == cardVisitOrder[orderNum][1]:
            distance += spot[2]
            newBoard[spot[0]][spot[1]] = 0
            q.clear()
            visited = [[False] * 4 for _ in range(4)]
            visited[spot[0]][spot[1]] = True
            if orderNum == len(cardVisitOrder) - 1:
                break

            q.append([cardVisitOrder[orderNum][0], cardVisitOrder[orderNum][1], 0])
            orderNum += 1
            continue

        # 한 칸 이동
        for i in range(4):
            nx = spot[0] + dx[i]
            ny = spot[1] + dy[i]
            if nx < 0 or nx >= 4 or ny < 0 or ny >= 4:
                continue
            if not visited[nx][ny]:
                visited[nx][ny] = True
                if nx == cardVisitOrder[orderNum][0] and ny == cardVisitOrder[orderNum][1]:
                    q.clear()
                    q.append([nx, ny, spot[2] + 1])
                else:
                    q.append([nx, ny, spot[2] + 1])

        # Ctrl 이동
        for i in range(4):
            nx = spot[0] + dx[i]
            ny = spot[1] + dy[i]
            if nx < 0 or nx >= 4 or ny < 0 or ny >= 4:
                continue
            while newBoard[nx][ny] == 0:
                nx += dx[i]
                ny += dy[i]
                if nx < 0 or nx >= 4 or ny < 0 or ny >= 4:
                    nx -= dx[i]
                    ny -= dy[i]
                    break

            if not visited[nx][ny]:
                visited[nx][ny] = True
                if nx == cardVisitOrder[orderNum][0] and ny == cardVisitOrder[orderNum][1]:
                    q.clear()
                    q.append([nx, ny, spot[2] + 1])
                else:
                    q.append([nx, ny, spot[2] + 1])

    return distance


def solution(board, r, c):
    global orderVisited
    cardList = set()
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                cardList.add(board[i][j])

    cardList = list(cardList)
    visitedCardList = [False] * len(cardList)
    setCardOrder(cardList, [], visitedCardList)

    cardSpots = getCardSpotAsDict(board)
    moveCount = []
    for cardOrder in cardOrders:
        orderVisited = []
        setSameCardOrder(cardOrder, cardSpots, [], 0)
        for cardVisitOrder in orderVisited:
            moveCount.append(bfs(cardVisitOrder, board, r, c))

    return min(moveCount) + len(cardList) * 2


# print(solution([[1, 0, 0, 3], [2, 0, 0, 0], [0, 0, 0, 2], [3, 0, 1, 0]], 1, 0))  # result : 14
# print(solution([[3, 0, 0, 2], [0, 0, 1, 0], [0, 1, 0, 0], [2, 0, 0, 3]], 0, 1))
# print(solution([[1, 0, 0, 3], [2, 0, 4, 0], [0, 4, 0, 2], [3, 0, 1, 0]], 1, 2))
# print(solution([[1, 5, 5, 3], [2, 0, 4, 0], [0, 4, 0, 2], [3, 0, 1, 0]], 1, 2))
print(solution([[1, 5, 5, 3], [2, 0, 4, 0], [0, 4, 6, 2], [3, 6, 1, 0]], 1, 2))