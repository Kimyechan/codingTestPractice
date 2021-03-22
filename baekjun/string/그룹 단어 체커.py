n = int(input())

count = 0
for i in range(n):
    word = input()
    wordMap = dict()

    isGroupWord = True
    prevAlphabet = ''
    for alphabet in word:
        if alphabet not in wordMap.keys():
            wordMap[alphabet] = 1
            prevAlphabet = alphabet
        elif alphabet in wordMap.keys() and alphabet != prevAlphabet:
            isGroupWord = False
            break

    if isGroupWord:
        count += 1

print(count)

# import sys
#
# num = int(sys.stdin.readline())
# count = num
# for _ in range(num):
#     string = sys.stdin.readline().rstrip()
#     alpha = []
#     for s in string:
#         if s not in alpha:
#             alpha.append(s)
#         elif alpha and s in alpha[:-1]:
#            count -= 1
#            break
# print(count)