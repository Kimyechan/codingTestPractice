# 0 -> 1 -> 2 -> 3

n, m = map(int, input().split())
r, c, d = map(int, input().split())

room = [list(map(int, input().split())) for _ in range(n)]
room[r][c] = 2

cleanCount = 1
while True:
    if room[r - 1][c] != 0 and room[r][c - 1] != 0 and room[r + 1][c] != 0 and room[r][c + 1] != 0:
        if d == 0:
            if room[r + 1][c] == 1:
                break
            else:
                r = r + 1
        elif d == 1:
            if room[r][c - 1] == 1:
                break
            else:
                c = c - 1
        elif d == 2:
            if room[r - 1][c] == 1:
                break
            else:
                r = r - 1
        elif d == 3:
            if room[r][c + 1] == 1:
                break
            else:
                c = c + 1
    else:
        d = (d + 3) % 4
        if d == 0:
            if room[r - 1][c] == 0:
                cleanCount += 1
                room[r - 1][c] = 2
                r = r - 1
        elif d == 1:
            if room[r][c + 1] == 0:
                cleanCount += 1
                room[r][c + 1] = 2
                c = c + 1
        elif d == 2:
            if room[r + 1][c] == 0:
                cleanCount += 1
                room[r + 1][c] = 2
                r = r + 1
        elif d == 3:
            if room[r][c - 1] == 0:
                cleanCount += 1
                room[r][c - 1] = 2
                c = c - 1

print(cleanCount)

# import sys
#
# input = sys.stdin.readline
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]
#
# def clean(x, y, d):
#     global ans
#     if a[x][y] == 0:
#         a[x][y] = 2
#         ans += 1
#     for _ in range(4):
#         nd = (d + 3) % 4
#         nx = x + dx[nd]
#         ny = y + dy[nd]
#         if a[nx][ny] == 0:
#             clean(nx, ny, nd)
#             return
#         d = nd
#     nd = (d + 2) % 4
#     nx = x + dx[nd]
#     ny = y + dy[nd]
#     if a[nx][ny] == 1:
#         return
#     clean(nx, ny, d)
#
#
# n, m = map(int, input().split())
# x, y, d = map(int, input().split())
# a = [list(map(int, input().split())) for _ in range(n)]
#
# ans = 0
# clean(x, y, d)
# print(ans)