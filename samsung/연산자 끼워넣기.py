# from itertools import combinations
#
# N = int(input())
# A = list(map(int, input().split(' ')))
# operators = list(map(int, input().split(' ')))
#
# L = -1000000000
# S = 1000000000

# operator = [4] * (N-1)
# used = [False] * (N-1)


# def combination(s):
#     if s == 3 and operators[s] == 0:
#         global L
#         global S
#         for index in range(N - 1):
#             if operator[index] == 0:
#                 A[index + 1] = A[index] + A[index + 1]
#             elif operator[index] == 1:
#                 A[index + 1] = A[index] - A[index + 1]
#             elif operator[index] == 2:
#                 A[index + 1] = A[index] * A[index + 1]
#             elif operator[index] == 3:
#                 if A[index] < 0:
#                     A[index + 1] = int(-1 * ((-1 * A[index]) / A[index + 1]))
#                 else:
#                     A[index + 1] = int(A[index] / A[index + 1])
#         L = max(L, A[-1])
#         S = min(S, A[-1])
#         return
#
#     v = s
#     x = operators[v]
#     for i in range(N-1):
#         if x == 0:
#             break
#
#         if not used[i] and operators[v] != 0:
#             x -= 1
#             operator[i] = v
#             used[i] = True
#         if x != 0:
#             combination(v)
#         else:
#             combination(v+1)
#
#
# combination(0)
#
#
# print(L)
# print(S)

# for index in range(N - 1):
#     if operator[index] == 0:
#         A[index + 1] = A[index] + A[index + 1]
#     elif operator[index] == 1:
#         A[index + 1] = A[index] - A[index + 1]
#     elif operator[index] == 2:
#         A[index + 1] = A[index] * A[index + 1]
#     elif operator[index] == 3:
#         if A[index] < 0:
#             A[index + 1] = int(-1 * ((-1 * A[index]) / A[index + 1]))
#         else:
#             A[index + 1] = int(A[index] / A[index + 1])

from itertools import permutations
import copy

N = int(input())
A = list(map(int, input().split(' ')))
operators = list(map(int, input().split(' ')))

operator = []
L = -1000000000
S = 1000000000

for i in range(4):
    for j in range(operators[i]):
        operator.append(i)

order = list(permutations(operator, N-1))

for X in order:
    B = copy.deepcopy(A)
    for index in range(N - 1):
        if X[index] == 0:
            B[index + 1] = B[index] + B[index + 1]
        elif X[index] == 1:
            B[index + 1] = B[index] - B[index + 1]
        elif X[index] == 2:
            B[index + 1] = B[index] * B[index + 1]
        elif X[index] == 3:
            if B[index] < 0:
                B[index + 1] = int(-1 * ((-1 * B[index]) / B[index + 1]))
            else:
                B[index + 1] = int(B[index] / B[index + 1])
    L = max(L, B[-1])
    S = min(S, B[-1])

print(L)
print(S)