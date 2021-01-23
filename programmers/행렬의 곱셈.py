def solution(arr1, arr2):
    result1 = []
    newArr2 = [[] for _ in range(len(arr2[0]))]

    for x in arr2:
        for i in range(len(x)):
            newArr2[i].append(x[i])

    for row in arr1:
        result2 = []
        for col in newArr2:
            sum = 0
            for i in range(len(row)):
                sum += row[i] * col[i]
            result2.append(sum)
        result1.append(result2)
    return result1

print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]))


def productMatrix(A, B):
    return [[sum(a*b for a, b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]