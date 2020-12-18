# from itertools import permutations, combinations -> 기억하기
from itertools import permutations


def solution(numbers):
    answer = 0

    numCom = []

    for i in range(len(numbers)):
        for com in permutations(numbers, i + 1):
            number = ""
            for num in com:
                number += num
            number = int(number)

            if number in numCom:
                continue
            else:
                numCom.append(number)
            flag = 0
            for i in range(2, number):
                if number % i == 0:
                    flag = 1
                    break
            if flag == 0 and number != 0 and number != 1:
                answer += 1

    return answer

print(solution("17"))