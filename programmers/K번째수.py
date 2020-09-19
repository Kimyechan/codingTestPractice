def solution(array, commands):
    answer = []
    sliceArray = []

    for command in commands:
        sliceArray = array[command[0]-1:command[1]]
        sliceArray.sort()
        answer.append(sliceArray[command[2]-1])

    return answer

print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))