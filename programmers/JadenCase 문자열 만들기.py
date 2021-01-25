def solution(s):
    answer = ""

    flag = 0
    for w in s:
        if w == " ":
            answer += " "
            flag = 0
        else:
            if flag == 0:
                answer += w.upper()
                flag = 1
            else:
                answer += w.lower()

    return answer


print(solution("   3people    unFollowed    me  "))