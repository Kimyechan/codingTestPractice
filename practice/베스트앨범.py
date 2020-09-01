def solution(genres, plays):
    genresHash = {}
    playsHashReverse = {}

    for i in range(len(genres)):
        if not genres[i] in genresHash.keys():
            genresHash[genres[i]] = list([i])
        else:
            temp = genresHash[genres[i]]
            temp.append(i)
            genresHash[genres[i]] = temp

    for i in range(len(plays)):
        playsHashReverse[i] = plays[i]

    maxList = []

    while True:
        currentMax = 0
        maxGenre = ""
        for key, value in genresHash.items():
            if key in maxList:
                continue
            genreSum = 0
            for index in value:
                genreSum += playsHashReverse[index]
            if currentMax < genreSum:
                currentMax = genreSum
                maxGenre = key
        maxList.append(maxGenre)
        if len(maxList) == len(genresHash.keys()):
            break

    result = []

    for genreName in maxList:
        if len(genresHash[genreName]) == 1:
            result.append(genresHash[genreName].pop(0))
        else:
            genreOrder = {}
            for num in genresHash[genreName]:
                genreOrder[num] = playsHashReverse[num]
            sort_orders = sorted(genreOrder.items(), key=lambda x: (x[1], -x[0]), reverse=True)
            for i in range(2):
                result.append(sort_orders[i][0])

    return result


print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 500, 500, 2500]))
