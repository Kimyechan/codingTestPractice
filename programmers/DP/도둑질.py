def solution(money):
    getMoney = [0] * len(money)

    # 첫번째집 방문
    getMoney[0] = money[0]
    getMoney[1] = money[0]
    for i in range(2, len(money) - 1):
        getMoney[i] = max(getMoney[i - 1], getMoney[i - 2] + money[i]) # 이전집 방문 했을 때, 안했을 때 중 최대값
    visit_first = getMoney[-2]

    # 첫번째집 방문 X, 두번째집 방문 O
    getMoney = [0] * len(money)
    getMoney[1] = money[1]
    for i in range(2, len(money)):
        getMoney[i] = max(getMoney[i - 1], getMoney[i - 2] + money[i])
    not_visit_first = getMoney[-1]

    # 첫번째집 방문 X, 두번째집 방문 X
    getMoney = [0] * len(money)
    for i in range(2, len(money)):
        getMoney[i] = max(getMoney[i - 1], getMoney[i - 2] + money[i])
    not_visit_first_second = getMoney[-1]

    answer = max(visit_first, not_visit_first, not_visit_first_second)

    return answer