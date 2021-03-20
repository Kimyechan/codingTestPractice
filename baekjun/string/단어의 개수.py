sentence = list(input().split(' '))

if sentence[0] == "":
    sentence.pop(0)

if sentence[-1] == "":
    sentence.pop()

print(len(sentence))

