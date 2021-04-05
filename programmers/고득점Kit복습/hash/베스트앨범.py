from collections import defaultdict


def solution(genres, plays):
    answer = []
    musicDict = defaultdict(list)
    musicPlayCount = defaultdict(int)

    for i in range(len(genres)):
        musicDict[genres[i]].append([plays[i], i])
        musicPlayCount[genres[i]] += plays[i]

    musicPlayCount = sorted(musicPlayCount.items(), key=lambda x: x[1], reverse=True)

    for genre, play in musicPlayCount:
        musicList = musicDict[genre]
        musicList.sort(key=lambda x: (x[0], -x[1]), reverse=True)
        if len(musicList) >= 2:
            answer.append(musicList[0][1])
            answer.append(musicList[1][1])
        else:
            answer.append(musicList[0][1])

    return answer


print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 500, 2500]))