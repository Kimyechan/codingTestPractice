def solution(s):
    maxLen = 1
    for center in range(len(s) - 1):
        countOdd = 0
        countEven = 0
        if s[center] == s[center + 1]:
            dis = 1
            countEven = 2
            while center - dis >= 0 and center + 1 + dis < len(s) \
                    and s[center - dis] == s[center + 1 + dis]:
                countEven += 2
                dis += 1
        dis = 1
        countOdd = 1
        while center - dis >= 0 and center + dis < len(s) \
                and s[center - dis] == s[center + dis]:
            countOdd += 2
            dis += 1

        maxLen = max([maxLen, countOdd, countEven])

    return maxLen