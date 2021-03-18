w = input()
alphabets = [-1] * (ord('z') - ord('a') + 1)

for i in range(len(w)):
    index = ord(w[i]) % ord('a')
    if alphabets[index] == -1:
        alphabets[index] = i

for a in alphabets:
    print(a, end=" ")