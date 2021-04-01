exp = list(input())

rank = {'+': 2, '-': 2, '*': 1, '/': 1, '(': 0, ')': 0}

stack = list()

for value in exp:
    if value == '+' or value == '-' or value == '*' or value == '/':
        if len(stack) == 0:
            stack.append(value)
        else:
            while len(stack) != 0 and rank[stack[-1]] <= rank[value] and stack[-1] != '(':
                print(stack.pop(), end="")
            stack.append(value)
    elif value == '(':
        stack.append(value)
    elif value == ')':
        while stack[-1] != '(':
            print(stack.pop(), end='')
        stack.pop()
    else:
        print(value, end='')

while stack:
    print(stack.pop(), end='')