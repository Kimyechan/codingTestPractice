t = int(input())

for _ in range(t):
    ps = list(input())

    stack = []
    for p in ps:
        if len(stack) == 0:
            stack.append(p)
        else:
            if p == ')' and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(p)

    if len(stack) == 0:
        print('YES')
    else:
        print('NO')