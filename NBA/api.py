import json

import requests

from match import Match

Match_List_Url = 'http://bifen4m.qiumibao.com/json/list.htm'


def match_list_request(url):
    response = requests.get(url)
    responseJson = json.loads(response.text)
    matchList = list()
    for matchJson in responseJson['list']:
        if matchJson['type'] == 'basketball' and matchJson['period_cn'] != '完赛':
            match = Match(**matchJson)
            matchList.append(match)
    return matchList


def main():
    matchList = match_list_request(Match_List_Url)
    match = matchList[0]
    print(match)


if __name__ == '__main__':
    main()
