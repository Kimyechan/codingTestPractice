skill = input()
skill_trees = input().split(' ')


def solution(skill, skill_trees):
    # C -> B -> D
    answer = 0
    for skill_tree in skill_trees:
        order = []
        right = True
        for i in range(len(skill_tree)):
            if skill_tree[i] in skill:
                order.append(skill.index(skill_tree[i]))

        if len(order) != 0 and skill[order[0]] in skill and skill[order[0]] != skill[0]:
            right = False

        for j in range(len(order) - 1):
            if order[j + 1] - order[j] != 1:
                right = False
                break

        if right:
            answer += 1

    return answer


print(solution(skill, skill_trees))
