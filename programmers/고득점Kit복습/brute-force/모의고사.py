def solution(answers):
    answer = []
    student1 = [1, 2, 3, 4, 5] * 2000
    student2 = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000

    correct = [0] * 3
    for i in range(len(answers)):
        if student1[i] == answers[i]:
            correct[0] += 1
        if student2[i] == answers[i]:
            correct[1] += 1
        if student3[i] == answers[i]:
            correct[2] += 1

    maxCorrect = max(correct)
    for idx, score in enumerate(correct):
        if maxCorrect == score:
            answer.append(idx + 1)

    return answer


print(solution([1, 2, 3, 4, 5]))
print(solution([1, 3, 2, 4, 2]))
