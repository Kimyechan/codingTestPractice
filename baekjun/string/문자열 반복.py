import sys
t = int(input())

for _ in range(t):
    r, s = sys.stdin.readline().split()
    r = int(r)

    result = ""
    for w in s:
        result += w * r

    print(result)