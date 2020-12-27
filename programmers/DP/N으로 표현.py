# N의 개수마다 만들 수 있는 값 -> 더 적은 N의 갯수로 만들 수 있는 값의 조합
def solution(N, number):
    array = [set() for i in range(8)]

    for idx, num in enumerate(array):
        num.add(int(str(N) * (idx + 1)))
        array[idx] = num

    for i in range(len(array)):
        for j in range(i):
            for op1 in array[j]:
                for op2 in array[i - j - 1]: # i, j -> 인덱스 // i - j -> 인덱스 위치 아님 // i - j - 1 -> 인덱스
                    array[i].add(op1 + op2)
                    array[i].add(op1 - op2)
                    array[i].add(op1 * op2)
                    if op2 != 0:
                        array[i].add(op1 // op2)
        if number in array[i]:
            answer = i + 1
            break
    else:
        answer = -1

    return answer

print(solution(5, 5))






















