t = int(input())

for _ in range(t):
    p = input()
    n = int(input())
    x = input()
    xArray = x[1:-1].split(",")

    error = False
    isReversed = False
    for calc in p:
        if calc == "R":
            if isReversed:
                isReversed = False
            else:
                isReversed = True
        else:
            if len(xArray) == 0 or (len(xArray) == 1 and xArray[0] == ""):
                error = True
                break
            else:
                if isReversed:
                    xArray.pop(-1)
                else:
                    xArray.pop(0)

    if error:
        print("error")
    else:
        result = "["
        if isReversed:
            xArray.reverse()
        for x in xArray:
            result += x + ","
        if result[-1] != ",":
            result += "]"
        else:
            result = result[:-1] + "]"
        print(result)