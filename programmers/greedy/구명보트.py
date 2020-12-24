## pop이나 del 쓰면 효율성 실패
# def solution(people, limit):
#     answer = 0
#     people.sort(reverse=True)
#
#     while people:
#         current = people.pop(0)
#         remain = limit - current
#
#         if people != [] and remain >= people[-1]:
#             people.pop(-1)
#
#         answer += 1
#
#     return answer


def solution(people, limit):
    answer = 0
    people.sort()
    i = 0
    j = len(people) - 1

    while i <= j:
        answer += 1
        if people[i] + people[j] <= limit:
            i += 1
        j -= 1

    return answer

print(solution([70, 50, 80, 50], 100))