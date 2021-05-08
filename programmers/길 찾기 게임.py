# check
# import sys
# sys.setrecursionlimit(10 ** 9)
#
#
# class Tree:
#     def __init__(self, x, y, num):
#         self.x = x
#         self.y = y
#         self.num = num
#         self.left = None
#         self.right = None
#
#
# preorderList = []
# postorderList = []
#
#
# def preorder(node):
#     preorderList.append(node.num + 1)
#     if node.left:
#         preorder(node.left)
#     if node.right:
#         preorder(node.right)
#
#
# def postorder(node):
#     if node.left:
#         postorder(node.left)
#     if node.right:
#         postorder(node.right)
#     postorderList.append(node.num + 1)
#
#
# def solution(nodeinfo):
#     answer = []
#     nodeInfoIndex = [(spot[0], spot[1], num) for num, spot in enumerate(nodeinfo)]
#     nodeInfoIndex.sort(key=lambda x: (-x[1], x[0]))
#     root = None
#     for node in nodeInfoIndex:
#         if not root:
#             root = Tree(node[0], node[1], node[2])
#         else:
#             x = node[0]
#             curNode = root
#             while True:
#                 if x < curNode.x:
#                     if curNode.left:
#                         curNode = curNode.left
#                         continue
#                     else:
#                         curNode.left = Tree(node[0], node[1], node[2])
#                         break
#                 if x > curNode.x:
#                     if curNode.right:
#                         curNode = curNode.right
#                         continue
#                     else:
#                         curNode.right = Tree(node[0], node[1], node[2])
#                         break
#                 break
#
#     preorder(root)
#     postorder(root)
#
#     answer.append(preorderList)
#     answer.append(postorderList)
#
#     return answer
import sys
sys.setrecursionlimit(10 ** 9)

preOrderList = []
postOrderList = []


class Tree:
    def __init__(self, x, y, num):
        self.x = x
        self.y = y
        self.num = num
        self.left = None
        self.right = None


def preOrder(root):
    preOrderList.append(root.num)
    if root.left:
        preOrder(root.left)
    if root.right:
        preOrder(root.right)


def postOrder(root):
    if root.left:
        postOrder(root.left)
    if root.right:
        postOrder(root.right)
    postOrderList.append(root.num)


def solution(nodeinfo):
    answer = []
    nodeinfo = [(value[0], value[1], num + 1) for num, value in enumerate(nodeinfo)]
    nodeinfo.sort(key=lambda x: (-x[1], x[0]))

    root = None
    for node in nodeinfo:
        x, y, num = node
        if root == None:
            root = Tree(node[0], node[1], node[2])
        else:
            cur = root
            while True:
                if cur.x > x:
                    if cur.left == None:
                        cur.left = Tree(node[0], node[1], node[2])
                        break
                    else:
                        cur = cur.left
                        continue
                if cur.x < x:
                    if cur.right == None:
                        cur.right = Tree(node[0], node[1], node[2])
                        break
                    else:
                        cur = cur.right
                        continue

    preOrder(root)
    postOrder(root)
    answer.append(preOrderList)
    answer.append(postOrderList)

    return answer

print(solution([[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]))
