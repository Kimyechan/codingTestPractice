n = int(input())

tree = dict()
for _ in range(n):
    node, left, right = input().split()
    tree[node] = (left, right)


def frontAround(node):
    if node not in tree.keys():
        return

    print(node, end="")
    frontAround(tree[node][0])
    frontAround(tree[node][1])


def centerAround(node):
    if node not in tree.keys():
        return

    centerAround(tree[node][0])
    print(node, end="")
    centerAround(tree[node][1])


def postAround(node):
    if node not in tree.keys():
        return

    postAround(tree[node][0])
    postAround(tree[node][1])
    print(node, end="")


frontAround('A')
print()
centerAround('A')
print()
postAround('A')