# check


def changeToSec(time):
    hour, minute, sec = time.split(":")
    result = int((int(hour) * 3600 + int(minute) * 60 + float(sec)) * 1000)
    return result


def solution(lines):
    times = []
    for line in lines:
        times.append(list(line.split(" ")))

    timesBetween = []
    totalTimesSeq = []
    for time in times:
        timeSecEnd = changeToSec(time[1])
        term = float(time[2].replace("s", "")) * 1000
        timeSecStart = int(timeSecEnd - term + 1)
        timesBetween.append([timeSecStart, timeSecEnd])
        print([timeSecStart, timeSecEnd])
        totalTimesSeq.append(timeSecStart)
        totalTimesSeq.append(timeSecEnd)

    result = 0
    for time in totalTimesSeq:
        count = 0
        start = int(time)
        end = int(time + 1000 -1)
        for timeBetween in timesBetween:
            if timeBetween[0] <= end and start <= timeBetween[1]: # timeBetween[0] <= start and end <= timeBetween[1] 범위 포함시키기 위해서
                count += 1
        if result < count:
            result = count

    return result


# def checktr(time, li):
#     c = 0
#     start = time
#     end = time + 1000
#     for i in li:
#         if i[1] >= start and i[0] < end:
#             c += 1
#     return c
#
#
# def solution(lines):
#     li = []
#     r = 1
#     for line in lines:
#         y, a, b = line.split()
#         a = a.split(':')
#         b = float(b.replace('s', '')) * 1000
#         end = (int(a[0]) * 3600 + int(a[1]) * 60 + float(a[2])) * 1000
#         start = end - b + 1
#         li.append([start, end])
#     for i in li:
#         r = max(r, checktr(i[0], li), checktr(i[1], li))
#     return r
