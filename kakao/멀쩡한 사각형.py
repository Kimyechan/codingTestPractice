# import math
# x, y = map(int, input().split(' '))
#
#
# def solution(w, h):
#     giulgi = math.ceil(h / w)
#     total = w * h
#     if giulgi != 1:
#         answer = total - giulgi * w
#         return answer
#     else:
#         makeOne = 0
#         checkValue = h / w
#         for i in range(1, h+1):
#             if checkValue * i == 1:
#                 answer = total - giulgi * h
#                 return answer
#             elif checkValue * i > 1:
#                 makeOne = i
#                 break
#         answer = total - (giulgi * w + math.trunc(h / makeOne))
#         return answer
#
#
# print(solution(x, y))

# import math
# x, y = map(int, input().split(' '))
#
#
# def solution(w, h):
#     total = w * h
#     lean = h / w
#     ban = 0
#
#     for i in range(w):
#         ban += math.ceil(lean * (i+1)) - math.trunc(lean * i)
#         # if math.ceil(lean * (i+1)) == math.trunc(lean * (i * 1)):
#         #     return i+1
#     answer = total - ban
#     return answer
#
#
# print(solution(x, y))

## 내가 못품
import math


def solution(w, h):
    if (w > h):
        w, h = h, w

    return w * h - (h + w - math.gcd(w, h))
















