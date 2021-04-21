from collections import deque


def solution(cacheSize, cities):
    time = 0
    caches = deque([0] * cacheSize)
    cities = deque(cities)

    if cacheSize == 0:
        return 5 * len(cities)

    while cities:
        city = cities.popleft()
        city = city.lower()
        if city not in caches:
            time += 5
            caches.popleft()
            caches.append(city)
        else:
            time += 1
            caches.remove(city)
            caches.append(city)

    return time


print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
print(solution(2,
               ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork",
                "Rome"]))
print(solution(5,
               ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork",
                "Rome"]))
print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))
