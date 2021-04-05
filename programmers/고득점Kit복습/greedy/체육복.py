def solution(n, lost, reserve):
    clotheCount = [1] * n

    for l in lost:
        clotheCount[l - 1] -= 1

    for r in reserve:
        clotheCount[r - 1] += 1

    for i in range(n):
        if clotheCount[i] == 2:
            if i == 0:
                if clotheCount[i + 1] == 0:
                    clotheCount[i] -= 1
                    clotheCount[i + 1] += 1
            elif i == n - 1:
                if clotheCount[i - 1] == 0:
                    clotheCount[i] -= 1
                    clotheCount[i - 1] += 1
            else:
                if clotheCount[i - 1] == 0:
                    clotheCount[i] -= 1
                    clotheCount[i - 1] += 1
                elif clotheCount[i] == 2 and clotheCount[i + 1] == 0:
                    clotheCount[i] -= 1
                    clotheCount[i + 1] += 1

    answer = 0
    for count in clotheCount:
        if count != 0:
            answer += 1

    return answer

# print(solution(5, [2, 4], [1, 3, 5]))
print(solution(3, [3], [1]))