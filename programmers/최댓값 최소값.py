def solution(s):
    # array = []
    # for x in s.split():
    #     array.append(int(x))

    array = list(map(int, input().split()))
    a = max(array)
    i = min(array)

    result = str(i) + " " + str(a)
    return result

print(solution("1 2 3 4"))
