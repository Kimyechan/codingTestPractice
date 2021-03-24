while True:
    line = input()
    if line == '.':
        break

    pList = [a for a in line if a in '[]()']
    stack = []
    for p in pList:
        if len(stack) == 0:
            stack.append(p)
        elif (stack[-1] == '(' and p == ')') or (stack[-1] == '[' and p == ']'):
            stack.pop()
        else:
            stack.append(p)

    if len(stack) == 0:
        print('yes')
    else:
        print('no')