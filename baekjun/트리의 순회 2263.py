# import sys
# sys.setrecursionlimit(1000000)
#
# n = int(input())
# inOrder = list(map(int, input().split()))
# postOrder = list(map(int, input().split()))
#
# index = [0] * (n + 1)
#
# for i in range(n):
#     index[inOrder[i]] = i
#
# preOrderResult = []
#
#
# def preOrder(inOrderStart, inOrderLast, postOrderStart, postOrderLast):
#     if inOrderStart > inOrderLast or postOrderStart > postOrderLast:
#         return
#
#     root = postOrder[postOrderLast]
#     preOrderResult.append(root)
#     left = index[root] - inOrderStart
#     # right = inOrderLast - index[root]
#
#     preOrder(inOrderStart, index[root] - 1, postOrderStart, postOrderStart + left - 1)
#     preOrder(index[root] + 1, inOrderLast, postOrderStart + left, postOrderLast - 1)
#     # preOrder(index[root] + 1, inOrderLast, postOrderLast - right, postOrderLast - 1)
#
#
# preOrder(0, n - 1, 0, n - 1)
# print(*preOrderResult)

import sys
sys.setrecursionlimit(1000000)

n = int(input())
inOrder = list(map(int, input().split()))
postOrder = list(map(int, input().split()))

index = [0] * (n + 1)

for i in range(n):
    index[inOrder[i]] = i

preOrderResult = []


def preOrder(inOrderStart, inOrderLast, postOrderStart, postOrderLast):
    if inOrderStart > inOrderLast or postOrderStart > postOrderLast:
        return

    root = postOrder[postOrderLast]
    preOrderResult.append(root)
    left = index[root] - inOrderStart

    preOrder(inOrderStart, index[root] - 1, postOrderStart, postOrderStart + left - 1)
    preOrder(index[root] + 1, inOrderLast, postOrderStart + left, postOrderLast - 1)


preOrder(0, n - 1, 0, n - 1)
print(*preOrderResult)

# import sys
#
# sys.setrecursionlimit(10 ** 9)
#
# n = int(sys.stdin.readline())
# inorder = list(map(int, sys.stdin.readline().split()))  # 중위순회
# postorder = list(map(int, sys.stdin.readline().split()))  # 후위순회
# in_location = [0 for _ in range(n + 1)]  # 인자를 찾을때 한번에 찾기위해서
# for i in range(n):
#     in_location[inorder[i]] = i
#
# tree = [[0, 0] for _ in range(n + 1)]  # 트리저장
#
#
# def find_tree(in_l, in_r, post_l, post_r):  # 중위순회 범위 후위순회 범위
#     if post_l <= post_r:
#         parents = postorder[post_r]  # 후위순회에서 부모노드 찾기
#         p_index = in_location[parents]
#         # for i in range(in_l,in_r+1):#인자찾기
#         #     if inorder[i]==parents:
#         #         p_index=i
#
#         l_count = p_index - in_l  # 왼쪽인자 갯수
#         if l_count > 0:  # 트리에 왼쪽자식노드 추가
#             tree[parents][0] = postorder[post_l + l_count - 1]
#         r_count = in_r - p_index  # 오른쪽인자 갯수
#         if r_count > 0:  # 트리에 왼쪽자식노드 추가
#             tree[parents][1] = postorder[post_r - 1]
#
#         find_tree(in_l, p_index - 1, post_l, post_l + l_count - 1)  # 부모노드를 기준으로 왼쪽노드
#         find_tree(p_index + 1, in_r, post_r - r_count, post_r - 1)  # 부모노드 기준 오른쪽
#
#
# find_tree(0, n - 1, 0, n - 1)
#
#
# # print(tree)
#
# def pre_order(start):
#     print(start, end=" ")
#     if tree[start][0] != 0:
#         pre_order(tree[start][0])
#     if tree[start][1] != 0:
#         pre_order(tree[start][1])
#
#
# pre_order(postorder[-1])
