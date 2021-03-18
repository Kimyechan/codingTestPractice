x = input()
y = input()

dpS = [list([''] * (len(y) + 1)) for _ in range(len(x) + 1)]

for i in range(1, len(x) + 1):
    for j in range(1, len(y) + 1):
        if x[i - 1] == y[j - 1]:
            dpS[i][j] = dpS[i-1][j-1] + x[i - 1]
        else:
            if len(dpS[i][j-1]) >= len(dpS[i-1][j]):
                dpS[i][j] = dpS[i][j - 1]
            else:
                dpS[i][j] = dpS[i - 1][j]

print(len(dpS[len(x)][len(y)]))
for w in dpS[len(x)][len(y)]:
    print(w, end="")
