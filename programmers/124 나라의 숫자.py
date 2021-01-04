# 0을 표현 가능하도록 n - 1을 진행, 각 자리수마다 0을 표현가능하도록 만듬
def solution(n):
    answer = ''
    otf = [1, 2, 4]
    result = []
    while n > 0:
        n = n - 1
        tenR = n % 3
        result.append(otf[tenR])
        n //= 3

    result.reverse()
    for i in result:
        answer += str(i)
    return answer

print(solution(3))