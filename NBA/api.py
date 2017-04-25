import json
from datetime import datetime

import requests

from match import Match

Match_List_Url = 'http://bifen4m.qiumibao.com/json/list.htm'
Match_Info_Url = 'http://bifen4pc2.qiumibao.com/json/%s/%s.htm'
Match_Max_Sid_Url = 'http://dingshi4pc.qiumibao.com/livetext/data/cache/max_sid/%s/0.htm'
Match_Living_Url = 'http://dingshi4pc.qiumibao.com/livetext/data/cache/livetext/%s/0/lit_page_2/%d.htm'


def match_list_request(url):
    response = requests.get(url)
    responseJson = json.loads(response.text)
    matchList = list()
    for matchJson in responseJson['list']:
        if matchJson['type'] == 'basketball':
            match = Match(**matchJson)
            matchList.append(match)
    return matchList


def match_info_request(url, match_id):
    today = datetime.now().strftime('%Y-%m-%d')
    response = requests.get(url % (today, match_id))
    mathInfo = json.loads(response.text)
    return mathInfo


def match_max_sid_request(url, match_id):
    response = requests.get(url % match_id)
    return int(response.text)


def match_living_request(url, match_id, match_sid):
    pass


def main():
    matchList = match_list_request(Match_List_Url)
    match = matchList[0]
    matchInfo = match_info_request(Match_Info_Url, match.id)
    matchMaxSid = match_max_sid_request(Match_Max_Sid_Url, match.id)
    print(matchMaxSid)


if __name__ == '__main__':
    main()
