# def solution(string):
#     answer = 1000
#     if len(string) == 1:
#         return 1
#
#     for s1 in range(1, len(string) // 2 + 1):
#         ret = ""
#         counter = 1
#
#         prev = string[:s1]
#
#         for i in range(s1, len(string) + s1, s1):
#             if prev == string[i:i + s1]:
#                 counter += 1
#             else:
#                 if counter != 1:
#                     ret = ret + str(counter) + prev
#                 else:
#                     ret = ret + prev
#                 prev = string[i:i + s1]
#                 counter = 1
#         answer = min(answer, len(ret))
#     return answer


def solution(string):
    answer = 1000
    if len(string) == 1:
        return 1

    for s1 in range(1, len(string) // 2 + 1):
        ret = ""
        counter = 1

        prev = string[:s1]

        for i in range(s1, len(string), s1):
            if prev == string[i:i + s1]:
                counter += 1
            else:
                if counter != 1:
                    ret = ret + str(counter) + prev
                else:
                    ret = ret + prev
                prev = string[i:i + s1]
                counter = 1
        if counter == 1:
            ret += prev
        else:
            ret += str(counter) + prev
        answer = min(answer, len(ret))
    return answer


print(solution("abcabcdede"))