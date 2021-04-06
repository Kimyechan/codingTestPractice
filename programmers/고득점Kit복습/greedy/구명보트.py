def solution(people, limit):
    people.sort()

    a = 0
    b = len(people) - 1
    boatCount = 0
    while a <= b:
        boatCount += 1
        if people[a] + people[b] <= limit and a != b:
            a += 1
        b -= 1

    return boatCount


print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50], 100))
print(solution([70, 50, 80, 50, 50, 60], 100))
print(solution([50, 50, 50, 50], 100))
