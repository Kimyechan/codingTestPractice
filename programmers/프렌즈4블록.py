# def solution(m, n, board):
#     answer = 0
#
#     for i in range(m):
#         board[i] = list(board[i])
#
#     while True:
#         isClear = False
#         clearSpots = set()
#         for i in range(m - 1):
#             for j in range(n - 1):
#                 current = board[i][j]
#                 if current != '' and current == board[i + 1][j] and current == board[i][j + 1] and current == board[i + 1][j + 1]:
#                     clearSpots.add((i, j))
#                     clearSpots.add((i + 1, j))
#                     clearSpots.add((i, j + 1))
#                     clearSpots.add((i + 1, j + 1))
#                     isClear = True
#
#         answer += len(clearSpots)
#
#         for clearSpot in list(clearSpots):
#             board[clearSpot[0]][clearSpot[1]] = ''
#
#         for i in range(n):
#             emptySpots = []
#             for j in range(m):
#                 if board[j][i] == '':
#                     emptySpots.append(j)
#
#             if emptySpots:
#                 swapIndex = emptySpots[-1]
#                 for j in range(0, emptySpots[0]):
#                     board[swapIndex][i], board[j][i] = board[j][i], board[swapIndex][i]
#                     swapIndex -= 1
#
#         if not isClear:
#             break
#
#     return answer


def solution(m, n, board):
    answer = 0

    newBoard = []
    for j in range(n):
        temp = []
        for i in range(m):
            temp.append(board[i][j])
        newBoard.append(temp)

    while True:
        isClear = False
        clearSpots = set()
        for i in range(n - 1):
            for j in range(m - 1):
                current = newBoard[i][j]
                if current != '' and current == newBoard[i + 1][j] and current == newBoard[i][j + 1] and current == newBoard[i + 1][j + 1]:
                    clearSpots.add((i, j))
                    clearSpots.add((i + 1, j))
                    clearSpots.add((i, j + 1))
                    clearSpots.add((i + 1, j + 1))
                    isClear = True

        answer += len(clearSpots)

        for clearSpot in list(clearSpots):
            newBoard[clearSpot[0]][clearSpot[1]] = ''

        for i in range(n):
            index = 0
            while index != m:
                if newBoard[i][index] == '':
                    newBoard[i].pop(index)
                    newBoard[i].insert(0, '')
                index += 1

        if not isClear:
            break

    return answer

# print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
# print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))
print(solution(5, 6, ["AAAAAA", "BBAATB", "BBAATB", "JJJTAA", "JJJTAA"]))