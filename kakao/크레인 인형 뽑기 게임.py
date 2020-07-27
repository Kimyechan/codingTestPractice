def solution(board, moves):
    answer = 0
    n = len(board[0])
    inputBox = []
    boardReversed = [[0 for _ in range(n)] for _ in range(n)]

    for j in range(n):
        temp = []
        for i in range(n):
            temp.append(board[i][j])
        boardReversed[j] = temp

    for i in range(n):
        while boardReversed[i][0] == 0:
            boardReversed[i].pop(0)

    for wide in moves:
        if len(boardReversed[wide - 1]) != 0:
            x = boardReversed[wide - 1].pop(0)
        else:
            x = 101
        if len(inputBox) != 0 and x == inputBox[len(inputBox) - 1]:
            answer += 2
            inputBox.pop()
        else:
            if x != 101:
                inputBox.append(x)
    return answer