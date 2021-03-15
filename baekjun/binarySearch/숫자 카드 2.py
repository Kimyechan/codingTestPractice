from collections import defaultdict

N = int(input())
cardHave = sorted(list(map(int, input().split())))
M = int(input())
cardGiven = list(map(int, input().split()))

cardMap = defaultdict(int)

for value in cardHave:
    if value not in cardMap.keys():
        cardMap[value] = 1
    else:
        cardMap[value] = cardMap[value] + 1

for valueFind in cardGiven:
    if valueFind in cardMap.keys():
        print(cardMap[valueFind], end=" ")
    else:
        print(0, end=" ")

# def binarySearch(cardList, value):
#     if len(cardList) == 0:
#         return 0
#
#     mid = len(cardList) // 2
#     if cardList[mid] == value:
#         return cardList.count(value)
#     else:
#         if cardList[mid] < value:
#             return binarySearch(cardList[mid + 1:], value)
#         else:
#             return binarySearch(cardList[:mid], value)
#
#
# cardMap = defaultdict(int)
# for value in cardGiven:
#     if value not in cardMap.keys():
#         cardMap[value] = binarySearch(cardHave, value)
#
# for countValue in cardMap.values():
#     print(countValue, end=" ")