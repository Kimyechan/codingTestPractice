import math


def solution(arr):
    answer = arr[0]
    for x in arr:
        answer = (x * answer) // math.gcd(x, answer)
    return answer

# 유클리드 호제법
# def solution(arr):
#     arr.sort(reverse=True)
#     for i in range(len(arr)-1):
#         a = arr[i]
#         b = arr[i+1]
#         while a%b:
#             r = a%b
#             a = b
#             b = r
#         arr[i+1] = (arr[i]*arr[i+1])/b
#     return arr[-1]


print(solution([2,6,8,14]))