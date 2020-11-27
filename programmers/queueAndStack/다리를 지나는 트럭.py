from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge_line = deque([0] * bridge_length)
    current_truck = []

    while True:
        current_weight = 0
        if bridge_line.popleft() != 0:
            if current_truck:
                current_truck.pop(0)

        for weightV in current_truck:
            current_weight += weightV
        value = 10001
        if truck_weights:
            value = truck_weights[0]

        if current_weight + value <= weight:
            value_w = truck_weights.pop(0)
            current_truck.append(value_w)
            bridge_line.append(value_w)
        else:
            bridge_line.append(0)

        answer += 1
        if not truck_weights:
            total = 0
            for line in bridge_line:
                total += line
            if total == 0:
                break

    return answer


print(solution(2, 10, [7,4,5,6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))