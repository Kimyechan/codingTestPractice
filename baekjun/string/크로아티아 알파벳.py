croatia = list(input())
croatia.reverse()

count = 0
i = 0
while i < len(croatia):
    if croatia[i] == '-':
        i += 2
        count += 1
    elif croatia[i] == '=':
        if i + 2 < len(croatia) and croatia[i + 1] == 'z' and croatia[i + 2] == 'd':
            i += 3
            count += 1
        else:
            i += 2
            count += 1
    elif croatia[i] == 'j':
        if i + 1 < len(croatia) and (croatia[i + 1] == 'n' or croatia[i + 1] == 'l'):
            i += 2
            count += 1
        else:
            i += 1
            count += 1
    else:
        i += 1
        count += 1

print(count)