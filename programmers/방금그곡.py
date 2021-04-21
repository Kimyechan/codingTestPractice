# check
from collections import deque


def solution(m, musicinfos):
    answer = ''

    mParse = parseMusic(m)

    musicParses = []
    for musicinfo in musicinfos:
        musicParse = []
        s = musicinfo.split(",")
        musicParse.append(s[0])
        musicParse.append(s[1])
        musicParse.append(s[2])

        temp = parseMusic(s[3])
        musicParse.append(temp)

        musicParses.append(musicParse)

    timeMax = 0
    for music in musicParses:
        startTime = music[0].split(":")
        endTime = music[1].split(":")
        time = 60 * (int(endTime[0]) - int(startTime[0])) + (int(endTime[1]) - int(startTime[1]))

        musicLen = len(music[3])
        musicLoop = []
        for i in range(time // musicLen):
            musicLoop.extend(music[3])
        musicLoop.extend(music[3][:time % musicLen])

        index = 0
        startIndex = 0
        index2 = 0
        while startIndex + index2 != len(musicLoop):
            if mParse[index] == musicLoop[startIndex + index2]:
                index += 1
                index2 += 1
            else:
                startIndex += 1
                index = 0
                index2 = 0

            if index == len(mParse):
                break

        if index == len(mParse):
            if time > timeMax:
                timeMax = time
                answer = music[2]

    if answer == '':
        return "(None)"
    else:
        return answer


def parseMusic(m):
    temp = []
    temp2 = deque(list(m))
    while temp2:
        v = temp2.popleft()
        if len(temp2) != 0 and temp2[0] == "#":
            v2 = temp2.popleft()
            temp.append(v + v2)
        else:
            temp.append(v)

    return temp


print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("cdcdf", ["12:00,12:14,HELLO,cdcdcdf"]))