def solution(prices):
    result = [0] * len(prices)
    stack = []

    for time, price in enumerate(prices):
        if len(stack) == 0:
            stack.append([time, price])
        else:
            while len(stack) != 0 and stack[-1][1] > price:
                downTime = stack.pop()
                result[downTime[0]] = time - downTime[0]
            stack.append([time, price])

    for remain in stack:
        result[remain[0]] = len(prices) - 1 - remain[0]

    return result


print(solution([1, 2, 3, 2, 3]))
