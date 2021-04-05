from collections import defaultdict


def solution(phone_book):
    answer = True

    # 존재하는 번호 체크
    phoneNumberDict = defaultdict(int)
    for phoneNumber in phone_book:
        phoneNumberDict[phoneNumber] = 1

    # 번호별 앞에서 길이별로 잘라서 갯수 체크
    numberHead = defaultdict(int)
    for phoneNumber in phone_book:
        for i in range(len(phoneNumber)):
            phoneNumberSlice = phoneNumber[:i + 1]
            if numberHead[phoneNumberSlice] == 1 and phoneNumberDict[phoneNumberSlice] == 1:
                answer = False
                break
            else:
                numberHead[phoneNumber[:i + 1]] += 1
        if not answer:
            break

    return answer


print(solution(["119", "97674223", "1195524421"]))