import api


def get_match():
    def get_match_list():
        match_list = api.match_list_request()
        for match in match_list:
            print(match)
        return match_list

    match_list = get_match_list()
    match_id = input('输入比赛ID:')

    for match in match_list:
        if match_id == match.id:
            return match_id
        else:
            print('输入ID有误')
            return 0


def get_match_text(match_id):
    currentSid = 0
    sid_set = set()
    while(True):
        sid = api.match_sid_request(match_id)
        if currentSid == sid:
            continue

        currentSid = sid
        liveTexts = api.match_living_request(match_id, currentSid)
        for liveText in liveTexts:
            if liveText.live_sid not in sid_set:
                print(liveText)
            sid_set.add(liveText.live_sid)


def main():
    match_id = get_match()
    if match_id != 0:
        get_match_text(match_id)


if __name__ == '__main__':
    main()
