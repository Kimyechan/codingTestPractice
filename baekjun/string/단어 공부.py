from collections import defaultdict

s = input()
s = s.lower()

alphabet = defaultdict(int)
for word in s:
    alphabet[word] += 1

result = []
maxCount = max(alphabet.values())
for word, count in alphabet.items():
    if maxCount == count:
        result.append(word)

if len(result) == 1:
    print(result[0].upper())
else:
    print("?")