# def solution(A, B):
#     answer = 0
#     A.sort()
#     B.sort()
#     n = len(A)
#
#     i = 0
#     j = 0
#     while i < n:
#         if B[j] > A[i]:
#             answer += 1
#             i += 1
#             j += 1
#         else:
#             while j < n:
#                 if B[j] > A[i]:
#                     answer += 1
#                     i += 1
#                     j += 1
#                     break
#                 j += 1
#             if j == n:
#                 break
#         if j == n:
#             break
#     return answer


def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    j = 0

    for i in range(len(A)):
        if A[j] < B[i]:
            answer = answer + 1
            j = j+1

    return answer

print(solution([5, 1, 3, 7], [2, 2, 6, 8]))
