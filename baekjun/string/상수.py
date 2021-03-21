A, B = input().split()
aList = list(A)
bList = list(B)

aList.reverse()
bList.reverse()

aReverse = ''
for num in aList:
    aReverse += num

bReverse = ''
for num in bList:
    bReverse += num

if int(aReverse) > int(bReverse):
    print(aReverse)
else:
    print(bReverse)