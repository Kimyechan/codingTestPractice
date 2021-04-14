# check
# from collections import deque
#
#
# def solution(bridge_length, weight, truck_weights):
#     bridge = deque(0 for _ in range(bridge_length))
#     total_weight = 0
#     step = 0
#     truck_weights.reverse()
#
#     while truck_weights:
#         total_weight -= bridge.popleft()
#         if total_weight + truck_weights[-1] > weight:
#             bridge.append(0)
#         else:
#             truck = truck_weights.pop()
#             bridge.append(truck)
#             total_weight += truck
#         step += 1
#
#     step += bridge_length
#
#     return step
# from collections import deque
#
#
# def solution(bridge_length, weight, truck_weights):
#     bridgeQ = deque([0 for _ in range(bridge_length)])
#     truckQ = deque(truck_weights)
#
#     totalWeight = 0
#     totalTime = 0
#
#     while truckQ:
#         totalWeight -= bridgeQ.popleft()
#         if totalWeight + truckQ[0] <= weight:
#             truckWeight = truckQ.popleft()
#             totalWeight += truckWeight
#             bridgeQ.append(truckWeight)
#         else:
#             bridgeQ.append(0)
#
#         totalTime += 1
#
#     totalTime += bridge_length
#
#     return totalTime
from collections import deque


def solution(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)

    totalTime = 0
    bridgeWeight = 0
    while truck_weights:
        bridgeWeight -= bridge.popleft()
        if bridgeWeight + truck_weights[0] <= weight:
            weightAdd = truck_weights.popleft()
            bridgeWeight += weightAdd
            bridge.append(weightAdd)
        else:
            bridge.append(0)
        totalTime += 1

    totalTime += bridge_length

    return totalTime


print(solution(2, 10, [7,4,5,6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))





















