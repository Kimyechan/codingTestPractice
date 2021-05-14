# check
import math


def solution(n, stations, w):
    answer = 0
    distances = []

    for i in range(1, len(stations)):
        distances.append((stations[i] - w) - (stations[i - 1] + w) - 1)

    distances.append(stations[0] - w - 1)
    distances.append(n - (stations[-1] + w))

    for distance in distances:
        if distance < 0:
            continue
        answer += math.ceil(distance / (w * 2 + 1))

    return answer