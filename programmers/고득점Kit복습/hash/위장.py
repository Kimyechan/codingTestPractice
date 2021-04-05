from collections import defaultdict


def solution(clothes):
    clotheKinds = defaultdict(int)

    for clothe in clothes:
        clotheKinds[clothe[1]] += 1

    clotheCombinationCount = 1
    for count in clotheKinds.values():
        clotheCombinationCount *= (count + 1)

    return clotheCombinationCount - 1


print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))