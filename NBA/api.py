import json
from datetime import datetime

import requests

from match import Match

Match_List_Url = 'http://bifen4m.qiumibao.com/json/list.htm'
Match_Info_Url = 'http://bifen4pc2.qiumibao.com/json/%s/%s.htm'


def match_list_request(url):
    response = requests.get(url)
    responseJson = json.loads(response.text)
    matchList = list()
    for matchJson in responseJson['list']:
        if matchJson['type'] == 'basketball' and matchJson['period_cn'] != '完赛':
            match = Match(**matchJson)
            matchList.append(match)
    return matchList


def match_info_request(url, match_id):
    today = datetime.now().strftime('%Y-%m-%d')
    response = requests.get(url % (today, match_id))
    mathInfo = json.loads(response.text)
    return mathInfo


def main():
    matchList = match_list_request(Match_List_Url)
    match = matchList[0]
    matchInfo = match_info_request(Match_Info_Url, match.id)
    print(matchInfo)


if __name__ == '__main__':
    main()
