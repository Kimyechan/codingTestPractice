# check
# from sys import stdin
# from collections import defaultdict, deque
#
# readline = stdin.readline
#
#
# def solve():
#     case = 1
#     while True:
#         edges = []
#         while True:
#             numbers = list(map(int, input().split()))
#             if numbers and numbers[-2:] == [0, 0]:
#                 edges += numbers[:-2]
#                 break
#             if numbers and numbers[-2:] == [-1, -1]:
#                 return
#             if numbers:
#                 edges += numbers
#         if check(edges):
#             print(f'Case {case} is a tree.')
#         else:
#             print(f'Case {case} is not a tree.')
#         case += 1
#
#
# def check(edges):
#     # 빈 트리
#     if not edges:
#         return True
#
#     in_degree = set()
#     nodes = set()
#     for i in range(0, len(edges), 2):
#         u, v = edges[i], edges[i + 1]
#         nodes.add(u)
#         nodes.add(v)
#         if v in in_degree:
#             return False
#         in_degree.add(v)
#     return len(nodes) == len(in_degree) + 1
#
#
# solve()

import sys


def check(edges):
    if not edges:
        return True

    inDegree = set()
    nodes = set()
    for i in range(0, len(edges), 2):
        u, v = edges[i], edges[i + 1]
        nodes.add(u)
        nodes.add(v)
        if v in inDegree:
            return False
        inDegree.add(v)

    if len(nodes) != len(inDegree) + 1:
        return False
    return True


def solution():
    count = 1
    while True:
        edges = []
        while True:
            temp = list(map(int, sys.stdin.readline().split()))
            if temp and temp[-2:] == [0, 0]:
                edges += temp[:-2]
                break
            if temp and temp[-2:] == [-1, -1]:
                return
            if temp:
                edges += temp

        if check(edges):
            print("Case %d is a tree." % count)
        else:
            print("Case %d is not a tree." % count)
        count += 1


solution()
