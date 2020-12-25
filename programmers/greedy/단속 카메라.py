# 틀린 문제 -> 자동차가 나가는 지점에 카메라 설치
def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1])
    camera = -30001

    for route in routes:
        if camera < route[0]:
            answer += 1
            camera = route[1]

    return answer