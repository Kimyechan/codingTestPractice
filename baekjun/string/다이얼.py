word = input()

dial = dict()
print(zip(['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']))
dial['ABC'] = 2
dial['DEF'] = 3
dial['GHI'] = 4
dial['JKL'] = 5
dial['MNO'] = 6
dial['PQRS'] = 7
dial['TUV'] = 8
dial['WXYZ'] = 9

time = 0
for a in word:
    for alphabet, number in dial.items():
        if a in alphabet:
            time += (number + 1)

print(time)
