def solution(s):
    opened = 0
    closed = 0

    for x in s:
        if x == '(':
            opened += 1
        elif x == ')':
            closed += 1
        if closed > opened:
            return False

    if opened == closed:
        return True
    else:
        return False

    return True