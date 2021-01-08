import sys
sys.setrecursionlimit(100000)
answer = [0, 0]


def compress(start, line, arr):
    one = 0
    zero = 0
    for i in range(line):
        for j in range(line):
            if arr[start[0] + i][start[1] + j] == 1:
                one += 1
            else:
                zero += 1

    if one == line * line:
        answer[1] += 1
        return
    elif zero == line * line:
        answer[0] += 1
        return
    else:
        compress([start[0], start[1]], line // 2, arr)
        compress([start[0] + line // 2, start[1]], line // 2, arr)
        compress([start[0], start[1] + line // 2], line // 2, arr)
        compress([start[0] + line // 2, start[1] + line // 2], line // 2, arr)


def solution(arr):
    global answer
    compress([0, 0], len(arr[0]), arr)
    return answer


print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))