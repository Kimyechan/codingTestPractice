import sys

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

teamList = []


def makeTeam(n, team):  # 백 트래킹
    if len(team) == n // 2:
        teamList.append(team[:])

    for player in range(n):
        if player not in team:
            if len(team) == 0 or (len(team) != 0 and player > team[-1]):
                team.append(player)
                makeTeam(n, team)
                team.pop()


makeTeam(N, [])
powerBetween = sys.maxsize
for i in range(len(teamList) // 2):
    startTeam = teamList[i]

    startTeamP = 0
    for player in startTeam:
        for j in range(N):
            if j in startTeam:
                startTeamP += S[player][j]

    linkTeam = teamList[-1 * i - 1]
    # linkTeam = [i for i in range(N)]
    # for j in startTeam:
    #     linkTeam.remove(j)
    linkTeamP = 0
    for player in linkTeam:
        for j in range(N):
            if j in linkTeam:
                linkTeamP += S[player][j]

    powerBetween = min(powerBetween, abs(startTeamP - linkTeamP))

print(powerBetween)
