# check
# def solution(n, t, m, timetable):
#     timetable = [int(time[:2]) * 60 + int(time[3:5]) for time in timetable]
#     timetable.sort()
#     last_time = (60 * 9) + (n - 1) * t
#
#     for i in range(n):
#         if len(timetable) < m:
#             return '%02d:%02d' % (last_time // 60, last_time % 60)
#         if i == n - 1:
#             if timetable[0] <= last_time:
#                 last_time = timetable[m - 1] - 1
#             return '%02d:%02d' % (last_time // 60, last_time % 60)
#         for j in range(m - 1, -1, -1):
#             bus_arrive = (60 * 9) + i * t
#             if timetable[j] <= bus_arrive:
#                 del timetable[j]
def solution(n, t, m, timetable):
    answer = 0
    timeMinute = [int(time[:2]) * 60 + int(time[3:5]) for time in timetable]
    timeMinute.sort()
    lastTime = 60 * 9 + t * (n - 1)

    for i in range(n):
        if len(timeMinute) < m:
            answer = lastTime
            break
        if i == n - 1:
            if timeMinute[m - 1] <= lastTime:
                lastTime = timeMinute[m - 1] - 1
            answer = lastTime
            break
        else:
            busTime = 60 * 9 + i * t
            for j in range(m - 1, -1, -1):
                if timeMinute[j] <= busTime:
                    del timeMinute[j]

    result = "%02d:%02d" % (lastTime // 60, lastTime % 60)
    return result
