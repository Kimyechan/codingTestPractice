def solution(record):
    answer = []
    userName = dict()

    for r in record:
        s = list(r.split())
        if s[0] == "Enter":
            userName[s[1]] = s[2]
        elif s[0] == "Change":
            userName[s[1]] = s[2]

    for r in record:
        s = list(r.split())
        if s[0] == "Enter":
            answer.append(userName[s[1]]+"님이 들어왔습니다.")
        elif s[0] == "Leave":
            answer.append(userName[s[1]]+"님이 나갔습니다.")

    return answer


print(solution(
    ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))
