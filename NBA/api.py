import json
from datetime import datetime

import requests

from match import Match
from liveText import LiveText

Match_List_Url = 'http://bifen4m.qiumibao.com/json/list.htm'
Match_Info_Url = 'http://bifen4pc2.qiumibao.com/json/%s/%s.htm'
Match_Sid_Url = 'http://dingshi4pc.qiumibao.com/livetext/data/cache/max_sid/%s/0.htm'
Match_Living_Url = 'http://dingshi4pc.qiumibao.com/livetext/data/cache/livetext/%s/0/lit_page_2/%d.htm'


def match_list_request():
    response = requests.get(Match_List_Url)
    responseJson = json.loads(response.text)
    matchList = list()
    for matchJson in responseJson['list']:
        if matchJson['type'] == 'basketball' and matchJson['period_cn'] != '完赛':
            match = Match(**matchJson)
            matchList.append(match)
    return matchList


def match_info_request(match_id):
    today = datetime.now().strftime('%Y-%m-%d')
    response = requests.get(Match_Info_Url % (today, match_id))
    mathInfo = json.loads(response.text)
    return mathInfo


def match_sid_request(match_id):
    response = requests.get(Match_Sid_Url % match_id)
    return int(response.text)


def match_living_request(match_id, match_sid):
    match_info = match_info_request(match_id)

    if match_sid % 2 != 0:
        match_sid += 1

    liveTexts = list()
    response = requests.get(Match_Living_Url % (match_id, match_sid))
    if response.status_code == 200:
        responseJson = json.loads(response.text)
        for liveJson in responseJson:
            liveText = LiveText(match_info, **liveJson)
            liveTexts.append(liveText)
    return liveTexts


def main():
    matchList = match_list_request()
    match = matchList[0]
    matchInfo = match_info_request(match.id)
    print(matchInfo)
    matchSid = match_sid_request(match.id)
    match_living_request(match.id, matchSid)


if __name__ == '__main__':
    main()
