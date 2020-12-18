# sort(reverse=True)
def solution(brown, yellow):
    answer = []
    totalB = brown + yellow
    len1 = 0
    len2 = 0

    for i in range(1, totalB + 1):
        if totalB % i == 0:
            len1 = totalB // i
            len2 = i
            if len1 < 2 or len2 < 2:
                continue
            if yellow == (len1 - 2) * (len2 - 2):
                answer = [len1, len2]
                break

    answer.sort(reverse=True)
    return answer


## 다른 사람 풀이
## red 사각형의 둘레길이 + 4 = brown의 갯수, red의 루트까지만 루프 -> 약수는 대칭
# def solution(brown, red):
#     for i in range(1, int(red**(1/2))+1):
#         if red % i == 0:
#             if 2*(i + red//i) == brown-4:
#                 return [red//i+2, i+2]