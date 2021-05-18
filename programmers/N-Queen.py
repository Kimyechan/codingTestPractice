import sys
sys.setrecursionlimit(10 ** 9)
answer = 0


def nQueen(row, n, spots):
    global answer
    if row == n:
        answer += 1
        return

    for col in range(n):
        possible = True
        for spot in spots:
            if col == spot[1]:
                possible = False
                break
            if abs(spot[0] - row) == abs(spot[1] - col):
                possible = False
                break

        if possible:
            spots.append([row, col])
            nQueen(row + 1, n, spots)
            spots.pop()


def solution(n):
    global answer
    nQueen(0, n, [])
    return answer


print(solution(4))
