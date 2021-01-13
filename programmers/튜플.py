# 다른 사람 풀이
def solution2(s):
    answer = []

    s1 = s.lstrip('{').rstrip('}').split('},{')

    new_s = []
    for i in s1:
        new_s.append(i.split(','))

    new_s.sort(key = len)

    for i in new_s:
        for j in range(len(i)):
            if int(i[j]) not in answer:
                answer.append(int(i[j]))

    return answer


def solution(s):
    answer = []
    s = s[1:len(s) - 1]
    array = s.split("{")
    array.sort(key=lambda x : len(x))
    array = array[1:len(array)]
    newArray = []
    for x in array:
        x = x.strip(",")
        x = x.strip("}")
        newArray.append(x)
    newArray2 = []
    for x in newArray:
        newArray2.append(x.split(","))
    for x in newArray2:
        for y in x:
            if int(y) not in answer:
                answer.append(int(y))
    return answer


print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))