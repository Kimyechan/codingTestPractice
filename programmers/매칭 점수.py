# check
import re
from copy import deepcopy


def solution(word, pages):
    basicScore = dict()
    pageIndexs = dict()
    pageLinks = dict()

    for idx, page in enumerate(pages):
        p1 = re.compile('<meta property="og:url" content="(\S+)"/>')
        metaContent = p1.findall(page)

        p2 = re.compile('<a href="(https://[\S]*)"')
        aHref = p2.findall(page)
        print(aHref)

        cnt = re.sub('[^a-zA-Z]', ' ', page).lower().split().count(word.lower())

        basicScore[metaContent[0]] = cnt
        pageIndexs[metaContent[0]] = idx
        pageLinks[metaContent[0]] = aHref

    totalScore = deepcopy(basicScore)
    for key, links in pageLinks.items():
        for link in links:
            if basicScore.get(link) is None:
                continue
            totalScore[link] = totalScore[link] + basicScore[key] / len(links)

    result = []
    for key, score in totalScore.items():
        result.append((pageIndexs[key], score))

    result.sort(key=lambda x: (-x[1], x[0]))

    return result[0][0]


# import re
# from copy import deepcopy
#
#
# def solution(word, pages):
#     basicScore = dict()
#     pageIndexs = dict()
#     pageLinks = dict()
#
#     for idx, page in enumerate(pages):
#         p1 = re.compile('<meta property="og:url" content="(.*?)"/>') # .*? -> 최소 일치 패턴, .* -> 최대 일치 패턴
#         metaContent = p1.findall(page)
#
#         p2 = re.compile('<a href="(.*?)"')
#         aHref = p2.findall(page)
#         print(aHref)
#
#         cnt = re.sub('[^a-zA-Z]', ' ', page).lower().split().count(word.lower())
#
#         basicScore[metaContent[0]] = cnt
#         pageIndexs[metaContent[0]] = idx
#         pageLinks[metaContent[0]] = aHref
#
#     totalScore = deepcopy(basicScore)
#     for key, links in pageLinks.items():
#         for link in links:
#             if basicScore.get(link) is None:
#                 continue
#             totalScore[link] = totalScore[link] + basicScore[key] / len(links)
#
#     result = []
#     for key, score in totalScore.items():
#         result.append((pageIndexs[key], score))
#
#     result.sort(key=lambda x: (-x[1], x[0]))
#
#     return result[0][0]

print(solution('blind', ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]))