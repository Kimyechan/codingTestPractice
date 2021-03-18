import re
p = re.compile('(100+1+|01)+')

n = int(input())
cases = [input() for _ in range(n)]

for case in cases:
    if p.fullmatch(case) is None:
        print("NO")
    else:
        print("YES")

