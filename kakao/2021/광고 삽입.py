def solution(play_time, adv_time, logs):
    play_time_sec = changeToSec(play_time)
    adv_time_sec = changeToSec(adv_time)

    logs_start_sec = []
    logs_end_sec = []
    for log in logs:
        logs_temp = log.split("-")
        logs_start_sec.append(changeToSec(logs_temp[0]))
        logs_end_sec.append(changeToSec(logs_temp[1]))

    total_time = [0] * (play_time_sec + 1)
    for i in range(len(logs_start_sec)):
        total_time[logs_start_sec[i]] = total_time[logs_start_sec[i]] + 1
        total_time[logs_end_sec[i]] = total_time[logs_end_sec[i]] - 1

    # i ~ i + 1 시간 사이의 누적 개수
    for i in range(1, play_time_sec + 1):
        total_time[i] = total_time[i] + total_time[i - 1]

    # 0 ~ i + 1 시간까지의 누적 시간
    for i in range(1, play_time_sec + 1):
        total_time[i] = total_time[i] + total_time[i - 1]

    max_time = 0
    max_start_time = 0
    for i in range(adv_time_sec, play_time_sec + 1):
        if i > adv_time_sec:
            if max_time < total_time[i] - total_time[i - adv_time_sec]:
                max_time = total_time[i] - total_time[i - adv_time_sec]
                max_start_time = i - adv_time_sec + 1
        else:
            if max_time < total_time[i]:
                max_time = total_time[i]
                max_start_time = 0

    result = changeToTime(max_start_time)
    return result


def changeToTime(max_time):
    hour = max_time // 3600
    max_time = max_time % 3600
    minute = max_time // 60
    max_time = max_time % 60
    sec = max_time
    return "{:02d}:{:02d}:{:02d}".format(hour, minute, sec)


def changeToSec(time):
    time_temp = time.split(":")
    play_time_sec = int(time_temp[0]) * 3600 + int(time_temp[1]) * 60 + int(time_temp[2])
    return play_time_sec


print(solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))
print(solution("99:59:59", "25:00:00", ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]))
print(solution("50:00:00", "50:00:00", ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]))