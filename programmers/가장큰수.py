def solution(numbers):
    sortedNumbers = merge_sort(numbers)
    answer = ""
    if sortedNumbers[0] == 0:
        answer = "0"
        return answer

    for value in sortedNumbers:
        answer += str(value)
    return answer


def merge_sort(array):
    if len(array) == 1:
        return array
    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    i, j, k = 0, 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1
    if i == len(left):
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
    elif j == len(right):
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
    return array


def compare(num1, num2):
    str1 = str(num1) + str(num2)
    str2 = str(num2) + str(num1)
    if int(str1) > int(str2):
        return True
    else:
        return False


print(solution([6, 10, 2]))
